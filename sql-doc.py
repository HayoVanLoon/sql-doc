#!/usr/bin/env /usr/bin/python3

# Copyright 2020 Hayo van Loon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import base64
import io
import os
import re
from typing import Dict, List, Optional, Set

COMMENT_TOKEN = '--'
DOCPATH_TOKEN = 'docpath'
DOCPATH_REGEX = re.compile(r'\s*docpath\s*[:= ]\s*(.+)')
DOCPATH_SPLIT_TOKEN = '/'
TAGS_TOKEN = 'tags'
TAGS_REGEX = re.compile(r'\s*tags\s*[:= ]\s*(.+)')
TAGS_SPLIT_TOKEN = ','
TAG_LINK_PREFIX = 'TAG'
ROOT = '.'
TAGS_SECTION = 'TAGS_SECTION'


class DocFile(object):

    def __init__(self, content: List[str],
                 code: List[str],
                 name: str,
                 real_path: str,
                 file_path: List[str],
                 doc_path: List[str],
                 tags: Set[str]) -> None:
        super().__init__()
        self.name = name
        self.link = str(base64.urlsafe_b64encode(bytes(real_path, 'utf-8')),
                        'utf-8')
        self.content = content
        self.code = code
        self.real_path = real_path
        self.file_path = file_path
        self._doc_path = doc_path
        self.tags = tags

    def path(self) -> List[str]:
        if self._doc_path:
            return self._doc_path[1:]
        else:
            return self.file_path[1:]


class Section(object):

    def __init__(self, docs: List[DocFile] = None,
                 sections: List = None) -> None:
        super().__init__()
        if not docs:
            docs = []
        if not sections:
            sections = []
        self.docs = docs
        self.sections = sections

    def name(self) -> str:
        return self.path()[-1]

    def path(self) -> List[str]:
        s = self
        lvl = 0
        while True:
            if s.docs:
                return s.docs[0].path()[:-1]
            if s.sections:
                s = s.sections[0]
                lvl += 1
            else:
                return []


class Tag(object):

    def __init__(self, name: str, docs: Set[DocFile]) -> None:
        super().__init__()
        self.name = name
        self.docs = docs


def is_hidden(p: str) -> bool:
    # TODO(hvl): might make more cross-platform
    base = os.path.basename(p)
    return len(base) > 2 and base[0] == '.'


def filter_path(path: str, no_symlink: bool) -> bool:
    if is_hidden(path):
        return False
    if no_symlink and os.path.islink(path):
        return False
    return True


def comment_line(line: str) -> bool:
    return line.startswith(COMMENT_TOKEN)


def is_doc_path(line: str) -> bool:
    return line.startswith(DOCPATH_TOKEN)


def process_doc_path(line: str) -> List[str]:
    x = DOCPATH_REGEX.findall(line)
    path = [ROOT]
    for item in x[0].split(DOCPATH_SPLIT_TOKEN):
        if item != ROOT and item:
            path.append(item.strip())
    return path


def is_tags(line: str) -> bool:
    return line.startswith(TAGS_TOKEN)


def process_tags(line: str) -> Set[str]:
    x = TAGS_REGEX.findall(line)
    tags = set()
    for item in x[0].split(TAGS_SPLIT_TOKEN):
        if item != ROOT and item:
            tags.add(item.strip())
    return tags


def process_file(src: str,
                 path: str,
                 ext: str,
                 no_symlink: bool) -> Optional[DocFile]:
    if not filter_path(path, no_symlink):
        return None
    if not path.endswith(ext):
        return None

    file_path = path[len(src) + 1:].split(os.sep)
    if file_path[0] != ROOT:
        file_path = [ROOT, *file_path]

    name = file_path[-1]

    content = []
    code = []
    doc_path = None
    tags = set()
    with open(path, 'r') as f:
        line = f.readline().strip()
        in_doc = True
        while line:
            stripped = line.strip()
            if stripped:
                in_doc = in_doc and comment_line(stripped)
                if in_doc:
                    clean = stripped[2:].strip()
                    if is_doc_path(clean):
                        doc_path = [*process_doc_path(clean), name]
                    elif is_tags(clean):
                        tags = tags.union(process_tags(clean))
                    else:
                        content.append(clean)
            if not in_doc:
                code.append(line)
            line = f.readline()

    return DocFile(content=content,
                   code=code,
                   name=name,
                   real_path=path,
                   file_path=file_path,
                   doc_path=doc_path,
                   tags=tags)


def process_dir(src: str, path: str, ext: str, no_symlink: bool) -> List[DocFile]:
    if is_hidden(path):
        return []

    result = []
    for p in os.listdir(path):
        file = os.path.join(path, p)
        if os.path.isdir(file):
            result.extend(process_dir(src, file, ext, no_symlink))
        else:
            df = process_file(src, file, ext, no_symlink)
            if df:
                result.append(df)

    return result


def organise(sorted_docs: List[DocFile], level: int) -> Section:
    grouped = {}
    docs = []
    for doc in sorted_docs:
        p = doc.path()
        if len(p) - level < 2:
            docs.append(doc)
        elif p and p[level] in grouped:
            grouped[p[level]].append(doc)
        else:
            grouped[p[level]] = [doc]

    sections = []
    for g in grouped:
        section = organise(grouped[g], level + 1)
        sections.append(section)

    return Section(docs=docs, sections=sections)


def get_tags(docs: List[DocFile]) -> Dict[str, Tag]:
    tags = {}
    for doc in docs:
        for t in doc.tags:
            if t in tags:
                tags[t].docs.add(doc)
            else:
                tags[t] = Tag(name=t, docs={doc})
    return tags


def markdown_index(current: Section, has_tags: bool, level: int = 0) -> str:
    buf = io.StringIO()
    if level == 0 and current.docs:
        buf.write(f'- [Root](#ROOT)\n')
    for section in current.sections:
        name = section.name()
        ref = DOCPATH_SPLIT_TOKEN.join(section.path())
        for i in range(level * 2):
            buf.write(' ')
        buf.write(f'- [{name}](#{ref})\n')
        buf.write(markdown_index(section, False, level + 1))
    if level == 0 and has_tags:
        buf.write(f'- [Tags](#{TAGS_SECTION})\n')
    return buf.getvalue()


def markdown_doc(doc: DocFile, out_diff: int) -> str:
    buf = io.StringIO()
    buf.write(f'<a name="{doc.link}"></a>\n')
    buf.write('######')
    buf.write(f' {doc.name}\n')
    p = ''
    for _ in range(out_diff):
        p = './.' + p
    buf.write(f'_[source]({p}{doc.real_path})_')
    for c in doc.content:
        buf.write(f'  \n{c}')
    if not doc.content:
        buf.write('\n\n_undocumented_')
    if doc.tags:
        buf.write('\n\ntags:')
    for t in doc.tags:
        buf.write(f' [{t}](#{TAG_LINK_PREFIX}{t})')
    if doc.code:
        buf.write('\n\n')
    for c in doc.code:
        buf.write(f'    {c}')
    return buf.getvalue()


def markdown_tag(tag: Tag) -> str:
    buf = io.StringIO()
    buf.write(f'<a name="{TAG_LINK_PREFIX}{tag.name}"></a>\n')
    buf.write(f'### {tag.name}\n')
    for doc in sorted(tag.docs, key=lambda x: x.real_path):
        buf.write(f'[{doc.name}](#{doc.link})\n')
    return buf.getvalue()


def markdown(current: Section,
             tags: Dict[str, Tag],
             out_diff: int,
             level: int = 0) -> str:
    buf = io.StringIO()

    if level == 0:
        # Write main header
        buf.write('# Query Documentation\n')
        buf.write(markdown_index(current, bool(tags), 0))
        buf.write('\n')

    # Write anchor
    ref = DOCPATH_SPLIT_TOKEN.join(current.path()) if level > 0 else "ROOT"
    buf.write(f'<a name="{ref}"></a>\n')

    if level > 0:
        # Write section header
        for i in range(min(6, level + 2)):
            buf.write('#')
        buf.write(f' {current.name()}')
        buf.write('\n')

    for doc in current.docs:
        buf.write(markdown_doc(doc, out_diff))
        buf.write('\n')

    for section in current.sections:
        buf.write(markdown(section, {}, out_diff, level + 1))
        buf.write('\n')

    if level == 0:
        if tags:
            buf.write(f'<a name="{TAGS_SECTION}"></a>\n')
            buf.write('## Tags\n')
        for t in tags:
            buf.write(markdown_tag(tags[t]))

    return buf.getvalue()


def main(src: str, ext: str, out: str, no_symlink: bool = True):
    if not src.startswith(ROOT):
        src = ROOT + '/' + src

    docs = process_dir(src, src, ext, no_symlink)
    sorted_docs = sorted(docs, key=lambda df: df.path())

    section = organise(sorted_docs, 0)
    tags = get_tags(sorted_docs)

    src_p = src.split(os.sep)
    out_p = out.split(os.sep)
    diff = 0
    for i in range(len(out_p) - 1):
        if i >= len(src_p) or src_p[i] != out_p[i]:
            diff += 1
    md = markdown(section, tags, diff)

    if not out:
        print(md)
    else:
        with open(out, 'w') as f:
            f.write(md)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A complete manual can be found at '
                    'https://github.com/HayoVanLoon/sql-doc')

    parser.add_argument(
        '--src',
        help='Path to sources root',
        default='.'
    )
    parser.add_argument(
        '--file_extension',
        help='SQL file extension',
        default='.sql'
    )
    parser.add_argument(
        '--out',
        help=('Output file, if left empty, writes to stdout.'
              'Used in source file link generation as well.'),
        default=''
    )
    # TODO(hvl): add flag for allowing symlink traversal

    args = parser.parse_args()
    params = args.__dict__

    main(src=params['src'], ext=params['file_extension'], out=params['out'],
         no_symlink=True)
