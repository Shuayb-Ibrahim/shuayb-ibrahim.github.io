---
layout: archive
title: "The SAVEPOINT statement"
permalink: /code/The_SAVEPOINT_statement
author_profile: true
redirect_from: The_RENAME_statement
---

A SAVEPOINT is a point in a transaction when you can roll the transaction back to a certain point without rolling back the entire transaction.

<u>The syntax for a SAVEPOINT command</u>
```sql
SAVEPOINT savepoint_name;
```

This command serves only in the creation of a SAVEPOINT among all the transactional statements. The ROLLBACK command is used to undo a group of transactions.

<u>The syntax for rolling back to a SAVEPOINT</u>
```sql
ROLLBACK TO savepoint_name
```

### <b><u>The RELEASE SAVEPOINT statement</u></b>
The RELEASE SAVEPOINT command is used to remove a SAVEPOINT that you have created.

<u>The syntax for a RELEASE SAVEPOINT</u>
```sql
RELEASE SAVEPOINT savepoint_name;
```

Once a SAVEPOINT has been released, you can no longer use the ROLLBACK command to undo transactions performed since the last SAVEPOINT.