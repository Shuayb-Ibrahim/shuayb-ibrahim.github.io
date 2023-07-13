---
layout: archive
title: "SQL Constraints"
permalink: /code/00_SQL/SQL_Constraints
author_profile: true
redirect_from: SQL_Constraints
---
# Constraints
SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

Constraints can be column level or table level. Column level constraints apply to a column, and table level constraints apply to the whole table.

<u>The following constraints are commonly used in SQL:</u>

-   [[The NOT NULL constraint]] - Ensures that a column cannot have a NULL value
-   [[The UNIQUE constraint]] - Ensures that all values in a column are different
-   [[The PRIMARY KEY constraint]] - A combination of a `NOT NULL` and `UNIQUE`, uniquely identifies each row in a table
-   [[The FOREIGN KEY constraint]] - Prevents actions that would destroy links between tables
-   [[The CHECK constraint]] - Ensures that the values in a column satisfies a specific condition
-   [[The DEFAULT constraint]] - Sets a default value for a column if no value is specified
