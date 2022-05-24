# The SELECT statement
<u>The SELECT-FROM statement</u>
```sql
SELECT column_name, ...
FROM table_name;
```

<u>The SELECT-FROM-WHERE statement</u>
```sql
SELECT *
FROM table_name
WHERE condition;
```

<u>The SELECT-FROM-WHERE statement with AND keyword</u>
```sql
SELECT *
FROM table_name
WHERE condition;
```

<u>The SELECT-FROM-WHERE statement with OR keyword</u>
```sql
SELECT *
FROM table_name
WHERE condition_1 OR condition_2;
```

<u>The SELECT-FROM-WHERE statement with IN/NOT IN keywords</u>
```sql
-- IN keyword 
SELECT *
FROM table_name
WHERE column_name IN (value_1, value_2,...);

-- NOT IN keyword 
SELECT *
FROM table_name
WHERE column_name NOT IN (value_1, value_2,...);
```

<u>The SELECT-FROM-WHERE statement with LIKE/NOT LIKE keywords</u>
```sql
-- LIKE keyword 
SELECT *
FROM table_name
WHERE column_name LIKE ('_value%');

-- NOT LIKE keyword 
SELECT *
FROM table_name
WHERE column_name NOT LIKE ('_value%');
```

<u>The SELECT-FROM-WHERE statement with BETWEEN-AND keywords</u>
```sql
SELECT * 
FROM table_name
WHERE column_name BETWEEN value_1 AND value_2;
```

<u>The SELECT-FROM-WHERE statement with IS NULL/IS NOT NULL keywords</u>
```sql
-- IS NULL keyword 
SELECT * 
FROM table_name
WHERE column_name IS NULL;

-- IS NOT NULL keyword
SELECT *
FROM table_name
WHERE column_name IS NOT NULL;
```

<u>The SELECT DISTINCT - FROM statement</u>
```sql
SELECT DISTINCT column_name
FROM table_name;
```

<u>The SELECT-FROM-ORDER BY statement</u>
```sql
SELECT *
FROM table_name
ORDER BY column_name [ASC/DESC];
```

<u>The SELECT-FROM-GROUP BY statement</u>
```sql
SELECT column_name, COUNT(column_name)
FROM table_name
GROUP BY column_name;
```

<u>The SELECT-FROM-GROUP BY-HAVING statement</u>
```sql
SELECT * 
FROM table_name
GROUP BY column_name
HAVING condition;
```

<u>The SELECT-FROM-LIMIT statement</u>
```sql
SELECT *
FROM table_name
LIMIT number_of_rows;
```
