---
layout: archive
title: "The COALESCE function"
permalink: /code/The_COALESCE_function
author_profile: true
redirect_from: The_COALESCE_function
---

The `COALESCE()` function is similar to [[The IFNULL() function]] but with more than two parameters. The function will always return a single value of the ones we have in the parentheses, and this value will be the first non-null value of a list of values (consisting of column name or strings/numbers) reading the values from left to right.

<u>The syntax for the coalesce function in [[The SELECT statement]] is:</u>

```sql
SELECT COALESCE(column_name, replacement_value1,replacement_value2, ..., replacement_valuen)
FROM table_name
WHERE condition;
```
