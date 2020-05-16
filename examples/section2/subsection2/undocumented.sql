SELECT
  name,
  num,
FROM UNNEST([
  STRUCT('foo' AS name, 42 AS num),
  STRUCT('bar' AS name, 3 AS num),
  STRUCT('fubar' AS name, 666 AS num)
])
