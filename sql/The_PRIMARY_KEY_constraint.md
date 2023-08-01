---
layout: archive
title: "The Primary Key constraint"
permalink: /code/The_PRIMARY_KEY_constraint
author_profile: true
redirect_from: The_PRIMARY_KEY_constraint
---

<u>The syntax to when creating a primary key in [[The CREATE statement]]:</u>

```sql
CREATE TABLE table_name (
column_name data_type,
...
 PRIMARY KEY (column_name)
);
```

<u>The syntax when changing the primary key in [[The ALTER statement]]:</u>

```sql
ALTER TABLE table_name 
ADD PRIMARY KEY (column_name);
```

<u>The syntax when dropping the primary key constraint using [[The DROP statement]]:</u>

```sql
ALTER TABLE table_name
DROP PRIMARY KEY;
```