---
layout: archive
title: "The INSERT statement"
permalink: /code/The_INSERT_statement
author_profile: true
redirect_from: The_INSERT_statement
---

<u>The INSERT INTO statement</u>
```sql
-- listing specific columns
INSERT INTO table_name (column_1, column_2, ...)
VALUES (value_1, value_2,...);

-- all columns
INSERT INTO table_name 
VALUES (value_1, value_2,...);
```

<u>The INSERT INTO - SELECT statement</u>
```sql
-- listing specific columns
INSERT INTO table_name_duplicate (column_1, column_2, ...)
SELECT *
FROM table_name;

-- all columns
INSERT INTO table_name_duplicate 
SELECT *
FROM table_name;
```
