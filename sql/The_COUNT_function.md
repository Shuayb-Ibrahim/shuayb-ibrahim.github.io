---
layout: archive
title: "The COUNT function"
permalink: /code/The_COUNT_function
author_profile: true
redirect_from: The_COUNT_function
---

The `COUNT()` function returns the number of rows that matches a specified criterion.

<u>The syntax for the count function in [[The SELECT statement]] is:</u>

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

There is also the `COUNT(DISTINCT)` function that helps you find the number of times unique values are encountered in a given column

<u>The syntax for the `COUNT(DISTINCT)` function in [[The SELECT statement]] is:</u>

```sql
SELECT COUNT(DISTINCT column_name)
FROM table_name
WHERE condition;
```

The `COUNT(*)` function returns all the rows in a table including null values. In the other examples, null values are excluded.

