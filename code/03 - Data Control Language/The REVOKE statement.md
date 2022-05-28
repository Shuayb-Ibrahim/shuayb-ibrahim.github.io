# The REVOKE statement
The Revoke statement is used to revoke some or all of the privileges which have been granted to a user in the past.

<u>The syntax for the REVOKE statement</u>
```sql
REVOKE privileges ON object FROM user;
```
Parameters Used:
- `privileges_name`: These are the access rights or [[Privileges]] granted to the user
- `object`: It is the name of the database object to which permissions are being granted. In the case of granting privileges on a table, this would be the table name.
- `user`: It is the name of the user to whom the privileges would be granted.
