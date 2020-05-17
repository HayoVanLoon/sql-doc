# Query Documentation

- [Root](#ROOT)
- [free](#free)
- [section1](#section1)
- [section2](#section2)
  - [subsection1](#section2/subsection1)
  - [subsection2](#section2/subsection2)
- [section3](#section3)
- [Tags](#TAGS_SECTION)
  - [animals.dogs](#TAGanimals.dogs)
  - [foods.fruits](#TAGfoods.fruits)

<a name="ROOT"></a>
<a name="Li9leGFtcGxlcy9yb290LnNxbA=="></a>
###### root.sql
_[source](./../examples/root.sql)_  
this is a root level file

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])

<a name="free"></a>
### free
<a name="Li9leGFtcGxlcy9ub3QtYS1zZWN0aW9uL3dpdGgtbmV3LWRvY3BhdGguc3Fs"></a>
###### with-new-docpath.sql
_[source](./../examples/not-a-section/with-new-docpath.sql)_  
this is a basic file with a new docpath

tags: [foods.fruits](#TAGfoods.fruits)

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])


<a name="section1"></a>
### section1
<a name="Li9leGFtcGxlcy9zZWN0aW9uMS93aXRoLWxlYWRpbmctc3BhY2VzLnNxbA=="></a>
###### with-leading-spaces.sql
_[source](./../examples/section1/with-leading-spaces.sql)_  
this is a basic file with leading spaces

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      -- ignored by the comment extraction
      STRUCT('fubar' AS name, 666 AS num)
    ])


<a name="section2"></a>
### section2
<a name="Li9leGFtcGxlcy9zZWN0aW9uMi9iYXNpYzIuc3Fs"></a>
###### basic2.sql
_[source](./../examples/section2/basic2.sql)_  
this is a basic file in section 2

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])

<a name="section2/subsection1"></a>
#### subsection1
<a name="Li9leGFtcGxlcy9zZWN0aW9uMi9zdWJzZWN0aW9uMS9tdWx0aS1saW5lLnNxbA=="></a>
###### multi-line.sql
_[source](./../examples/section2/subsection1/multi-line.sql)_  
this is a basic file in section 2.1  
with multiple lines

tags: [animals.dogs](#TAGanimals.dogs) [foods.fruits](#TAGfoods.fruits)

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])


<a name="section2/subsection2"></a>
#### subsection2
<a name="Li9leGFtcGxlcy9zZWN0aW9uMi9zdWJzZWN0aW9uMi9iYXNpYzIyLnNxbA=="></a>
###### basic22.sql
_[source](./../examples/section2/subsection2/basic22.sql)_  
this is a basic file in section 2.2

tags: [animals.dogs](#TAGanimals.dogs)

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])

<a name="Li9leGFtcGxlcy9zZWN0aW9uMi9zdWJzZWN0aW9uMi91bmRvY3VtZW50ZWQuc3Fs"></a>
###### undocumented.sql
_[source](./../examples/section2/subsection2/undocumented.sql)_

_undocumented_

    SELECT      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])



<a name="section3"></a>
### section3
<a name="Li9leGFtcGxlcy9ub3QtYS1zZWN0aW9uL3NlY3Rpb24zL3dpdGgtZG9jcGF0aC1jb3JyZWN0aW9uLnNxbA=="></a>
###### with-docpath-correction.sql
_[source](./../examples/not-a-section/section3/with-docpath-correction.sql)_  
this is a basic file with a docpath correction

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])


<a name="TAGS_SECTION"></a>
## Tags

<a name="TAGfoods.fruits"></a>
### foods.fruits
[with-new-docpath.sql](#Li9leGFtcGxlcy9ub3QtYS1zZWN0aW9uL3dpdGgtbmV3LWRvY3BhdGguc3Fs)
[multi-line.sql](#Li9leGFtcGxlcy9zZWN0aW9uMi9zdWJzZWN0aW9uMS9tdWx0aS1saW5lLnNxbA==)

<a name="TAGanimals.dogs"></a>
### animals.dogs
[multi-line.sql](#Li9leGFtcGxlcy9zZWN0aW9uMi9zdWJzZWN0aW9uMS9tdWx0aS1saW5lLnNxbA==)
[basic22.sql](#Li9leGFtcGxlcy9zZWN0aW9uMi9zdWJzZWN0aW9uMi9iYXNpYzIyLnNxbA==)

