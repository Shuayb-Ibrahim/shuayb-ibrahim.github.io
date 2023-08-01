---
layout: archive
title: "The Foregin Key constraint"
permalink: /code/The_FOREIGN_KEY_constraint
author_profile: true
redirect_from: The_FOREIGN_KEY_constraint
---

<u>The syntax to when creating a foreign key in [[The CREATE statement]]:</u>

```sql
CREATE TABLE table_1 (
column_name data_type,
...
 FOREIGN KEY (column_name) REFERENCES table_2(column_name) ON DELETE CASCADE
);
```

<u>The syntax when changing the foreign key in [[The ALTER statement]]:</u>

```sql
ALTER TABLE table_1 
ADD FOREIGN KEY (column_name) REFERENCES table_2(column_name) ON DELETE CASCADE;
```

<u>The syntax when dropping the foreign key constraint using the [[The DROP statement]]:</u>

```sql
ALTER TABLE table_name
DROP FOREIGN KEY column_name [IN DDL SETTING];
```

##### Related constraints: [[The ON DELETE CASCADE constraint]]

