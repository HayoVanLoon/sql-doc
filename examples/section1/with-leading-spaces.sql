  -- this is a basic file with leading spaces
SELECT
  name,
  num,
FROM UNNEST([
  STRUCT('foo' AS name, 42 AS num),
  STRUCT('bar' AS name, 3 AS num),
  -- ignored by the comment extraction
  STRUCT('fubar' AS name, 666 AS num)
])
