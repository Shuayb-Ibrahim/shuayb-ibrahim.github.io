---
layout: archive
title: "The GRANT statement"
permalink: /code/The_GRANT_statement
author_profile: true
redirect_from: The_GRANT_statement
---

To grant privileges to a user account, the GRANT statement is used. 

<u>The syntax for the GRANT statement</u> 
```sql
GRANT privileges_names ON object TO user;
```
Parameters Used:
- `privileges_name`: These are the access rights or [[Privileges]] granted to the user
- `object`: It is the name of the database object to which permissions are being granted. In the case of granting privileges on a table, this would be the table name.
- `user`: It is the name of the user to whom the privileges would be granted.

