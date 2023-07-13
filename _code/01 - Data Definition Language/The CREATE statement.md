# The CREATE statement
 <u>The syntax for creating a database:</u>
```sql
	-- Creating a database 
	CREATE [IF NOT EXISTS] DATABASE database_name; 
	--Creating a Schema (identical to create database statement) 
	CREATE [IF NOT EXISTS] SCHEMA database_name;
```
<u>The syntax for creating a table:</u>
``` sql
--Creating a table 
CREATE TABLE table_name ( 
column_1 data_type constraints, 
column_2 data_type constraints, 
... 
column_n data_type constraints, 
[Further constraints] );

-- Constraints 
[NULL/ NOT NULL / AUTO_INCREMENT / DEFAULT *value*]

-- Further constraints 
PRIMARY KEY(column_1) FOREIGN KEY(column_2) REFERENCES tablename(column_2) ON DELETE CASCADE UNIQUE KEY(column_3)
```

