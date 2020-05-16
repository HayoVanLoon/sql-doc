# Query Documentation
- [general](#ROOT)
- [free](#free)
- [section1](#section1)
- [section2](#section2)
  - [subsection1](#section2/subsection1)
  - [subsection2](#section2/subsection2)
- [section3](#section3)

<a name="ROOT"></a>
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
###### with-new-docpath.sql
_[source](./../examples/not-a-section/with-new-docpath.sql)_  
this is a basic file with a new docpath

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
###### with-leading-spaces.sql
_[source](./../examples/section1/with-leading-spaces.sql)_  
this is a basic file with leading spaces

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])


<a name="section2"></a>
### section2
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
###### multi-line.sql
_[source](./../examples/section2/subsection1/multi-line.sql)_  
this is a basic file in section 2.1  
with multiple lines

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
###### basic22.sql
_[source](./../examples/section2/subsection2/basic22.sql)_  
this is a basic file in section 2.2

    SELECT
      name,
      num,
    FROM UNNEST([
      STRUCT('foo' AS name, 42 AS num),
      STRUCT('bar' AS name, 3 AS num),
      STRUCT('fubar' AS name, 666 AS num)
    ])

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


