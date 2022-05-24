# The UNIQUE constraint
<u>The syntax when using unique in [[The CREATE statement]]:</u>

```sql
CREATE TABLE table_name (
column_name data_type,
...
UNIQUE KEY (column_name)
);
```

<u>The syntax when using unique in [[The ALTER statement]]:</u>

```sql
ALTER TABLE table_name 
ADD UNIQUE KEY (column_name);
```

<u>The syntax to drop a unique constraint on a column using [[The DROP statement]]:</u>

```sql
ALTER TABLE table_name
DROP INDEX column_name;
```