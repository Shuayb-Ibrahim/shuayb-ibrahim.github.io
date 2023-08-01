---
layout: archive
title: "The NOT NULL constraint"
permalink: /code/The_NOT_NULL_constraint
author_profile: true
redirect_from: The_NOT_NULL_constraint
---

<u>The syntax when using the not null constraint in the [[The CREATE statement]]</u>:
```sql
CREATE TABLE table_name ( 
column_name data_type NOT NULL,
... 
);
```

<u>The syntax when using the not null constraint in the [[The ALTER statement]]:</u>
```sql
ALTER TABLE table_name 
MODIFY column_name data_type NOT NULL;
```
