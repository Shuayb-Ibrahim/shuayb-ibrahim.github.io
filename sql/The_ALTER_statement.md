---
layout: archive
title: "The ALTER statement"
permalink: /code/The_ALTER_statement
author_profile: true
redirect_from: The_ALTER_statement
---

<u>The syntax to add a column to an already existing table:</u>
```sql
-- Adding a column to the table 
ALTER TABLE table_name 
ADD COLUMN column_2 data_type [AFTER column_2];
```

<u>The syntax to delete a column from an already existing table:</u>
```sql
-- Deleting a column from a table
ALTER TABLE table_name
DROP COLUMN column_name;
```

<u>The MODIFY keyword</u>
The `MODIFY` keyword allows us to manipulate two properties:
1. The data type
2. The constraints
```sql
-- Changing a column in the table
ALTER TABLE table_name
MODIFY column_name data_type constraints;
```

<u>The CHANGE keyword</u>
The `CHANGE` keyword allows us to manipulate three properties:
1. The name of the column
2. The data type
3. The constraints
```sql
	-- Changing a column in the table
ALTER TABLE table_name
CHANGE COLUMN column_name column_name* data_type constraints;
```

<u>The difference between MODIFY and CHANGE COLUMN</u>
In the `CHANGE` syntax statement above, we had to change the field name as well other details. Omitting the field name from the `CHANGE` statement will generate an error. 

Suppose we are only interested in changing the data type and constraints on the field without affecting the field name, we can use the `MODIFY` keyword to accomplish that.