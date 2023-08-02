---
layout: archive
title: "SQL Joins"
permalink: /code/SQL_Joins
author_profile: true
redirect_from: SQL_Joins
---

A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

The types of Joins you will find in SQL are:

-   `INNER JOIN`: Returns records that have matching values in both tables
-   `LEFT JOIN`: Returns all records from the left table, and the matched records from the right table
-   `RIGHT JOIN`: Returns all records from the right table, and the matched records from the left table
-   `CROSS JOIN`: Returns all records from both tables
-   `SELF JOIN`: Returns records that have matching values in the same table
-   `UNION/UNION ALL`: Combines the result-set of two or more SELECT statements.

![SQL Joins](different_joins_in_sql.png)
###### Inner Join

<u>The syntax for an inner join with two or more tables in [[The SELECT statement]]:</u>

```sql
-- two tables
SELECT column_name(s)
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name;

-- two plus tables
SELECT column_name(s)
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name
INNER JOIN table3 ON table1.column_name - table3.column_name
[etc];
```

###### Left Join

<u>The syntax for a left join in [[The SELECT statement]]</u>

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

###### Right Join

<u>The syntax for a right join in [[The SELECT statement]]</u>

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

###### Cross Join

<u>The syntax for a cross join in [[The SELECT statement]]</u>

```sql
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
```

**It is common practice to use Aliases on table names when using JOINS! **

Example:

```sql
-- Inner Join example from Employees Database
SELECT 
    m.dept_no, m.emp_no, d.dept_name
FROM
    dept_manager_dup m
        INNER JOIN
    departments_dup d ON m.dept_no = d.dept_no
ORDER BY dept_no;
```

###### Self Join
<u>The syntax for a self join in [[The SELECT statement]]</u>

```sql
SELECT column_name(s)
FROM table1 T1, table1 T2 -- T1 and T2 are different table aliases for the same table.
WHERE condition;
```

###### Union and Union All
<u>The syntax for a Union of two result-sets with distinct records</u>

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

<u>The syntax for a Union of two result-sets with All existing records</u>

```sql
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```