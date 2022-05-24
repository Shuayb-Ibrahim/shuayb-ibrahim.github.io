# The CHECK constraint
The `Check` constraint is used to specify a predicate that every tuple must satisfy in a given relation. It limits the values that a column can hold in a relation.

-   The predicate in check constraint can hold a sub query.
-   Check constraint defined on an attribute restricts the range of values for that attribute.
-   If the value being added to an attribute of a tuple violates the check constraint, the check constraint evaluates to false and the corresponding update is aborted.
-   Check constraint is generally specified with the CREATE TABLE command in SQL.

<u>The syntax for the Check constraint:</u>
```sql
CREATE TABLE table_name (
column_name data_type,
...
CHECK(column_name IN (option_a, option_b, option_c))
);
```

The check constraint in the above SQL command restricts the `column_name` to belong to only the categories specified. If a new tuple is added or an existing tuple in the relation is updated with an entry that doesn’t belong to any of the three options mentioned, then the corresponding database update is aborted.