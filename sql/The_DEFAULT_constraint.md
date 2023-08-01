---
layout: archive
title: "The DEFAULT constraint"
permalink: /code/The_DEFAULT_constraint
author_profile: true
redirect_from: The_DEFAULT_constraint
---

<u>The syntax when adding the Default constraint in [[The CREATE statement]]:</u>

```sql
CREATE TABLE table_name (
column_name data_type DEFAULT default_value
...
);
```

<u>The syntax when changing the Default constraint in [[The ALTER statement]]:</u>

```sql
ALTER TABLE table_name 
ALTER column_name SET DEFAULT default_value;
```

<u>The syntax when dropping the Default constraint using the [[The DROP statement]]:</u>

```sql
ALTER TABLE table_name 
ALTER column_name DROP DEFAULT;
```
