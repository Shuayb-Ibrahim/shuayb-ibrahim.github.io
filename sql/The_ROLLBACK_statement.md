---
layout: archive
title: "The ROLLBACK statement"
permalink: /code/The_ROLLBACK_statement
author_profile: true
redirect_from: The_ROLLBACK_statement
---

The ROLLBACK command is the transactional command used to undo transactions that have not already been saved to the database. This command can only be used to undo transactions since the last COMMIT or ROLLBACK command was issued.

<u>The syntax for a ROLLBACK command</u>
```sql
ROLLBACK;
```
