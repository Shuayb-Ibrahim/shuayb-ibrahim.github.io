---
layout: archive
title: "The IFNULL function"
permalink: /code/The_IFNULL_function
author_profile: true
redirect_from: The_IFNULL_function
---

The `IFNULL()` function returns the first of the two indicated values if the data value found in the table is not null, and returns the second value if there is a null value.

<u>The syntax for the if null function in [[The SELECT statement]] is:</u>

```sql
SELECT IFNULL(column_name, replacement_value)
FROM table_name
WHERE condition;
```

