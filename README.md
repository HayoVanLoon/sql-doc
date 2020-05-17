# SQL Docq

A script for generating (somewhat) structured Markdown documentation from 
comments in a pile of SQL files.

The script will traverse directories recursively. It extracts comments from SQL 
files, bundling them by location.   

The script has been designed for simplicity. It does not require changing how 
you write, format or structure your queries. It will hardly look at those; it
only cares for simple comments at the top of your SQL files.

Special keywords have been kept to a minimum, so you can focus on writing good 
comments, not memorising yet another set of keywords.

Inspired by protoc-gen-doc (https://github.com/pseudomuto/protoc-gen-doc)

Requires Python 3; tested with 3.6. Tested with GitHub.

## Usage
As simple as:
```bash
python3 sql-docq.py --src=examples --out=examples/README.md
```

You can also write to stdout by leaving out the `out` parameter:
```bash
python3 sql-docq.py --src=examples
```

By default, the script search for files ending in `.sql`.
This can be overridden with (include the dot):
```bash
python3 sql-docq.py --src=examples --file_extension=.foo --out=examples/README.md
```

## Documenting Example
Just add comments to the top of your query file.
```sql
-- Returns the current time.
-- This is done in a convoluted way, but the reason is: 'meh'.
-- tags: useless-queries poor-examples
SELECT 
  *
-- this comment is initially ignored, but will show up in the code block.
FROM
  UNNEST([CURRENT_TIME()])
```


## Rules
### Comment Parsing

- Blank lines are ignored.
- Starting from the top of the file, comment lines are added to the comment block.
- Once a non-comment appears, the remainder, including later comments, is added to the code block.
- Files without (starting) comments will still be included.
- Lines are *not sanitised* during parsing, only formatted.

### Section Creation

- Each directory below the sources root (`src`) forms a section, iff there is
at least one SQL file in it.
- Subdirectories become subsections.
- This behaviour is overridden with a special `docpath` keyword (see below).

### Special Keywords

#### docpath
The `docpath` keyword overrides the section determination logic for the file.

Example: `-- docpath: foo/bar` will place the file in the subsection `bar` of 
the section `foo`.

#### tags
The `tags` keyword allows for random, unstructured tagging. A common use would 
be to tag the tables touched by the query. You can then trace table 
dependencies. The keyword is to be followed with a comma-separated list (or a 
single item).

Example: `-- tags: foods.fruits, animals.dogs` will link the query with those 
two tags and vice versa. 


## License
Copyright 2020 Hayo van Loon

Licensed under the Apache License, Version 2.0 (the "License"); you may not use 
this file except in compliance with the License. You may obtain a copy of the 
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed 
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR 
CONDITIONS OF ANY KIND, either express or implied. See the License for the 
specific language governing permissions and limitations under the License.