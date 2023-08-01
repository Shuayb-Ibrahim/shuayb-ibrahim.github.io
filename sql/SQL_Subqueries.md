---
layout: archive
title: "SQL Subqueries"
permalink: /code/SQL_Subqueries
author_profile: true
redirect_from: SQL_Subqueries
---

Subqueries are also known as inner queries, nested queries and inner select statements. They are ultimately queries embedded in a query. They are part of another query query called the outer query also known as the outer select statement.

An example of a subquery with in keyword in the where clause of a select statement:

```sql
-- Example from Employees Database
SELECT e.first_name. e.last_name
FROM employees e
WHERE e.emp_no IN (SELECT
						dm.emp_no
				   FROM
					    dept_manager dm);
```

An example of a subquery with exists-not exists keyword in the where clause of a select statement:

```sql
-- Example from the Employees Database
SELECT 
    e.first_name, e.last_name
FROM
    employees e
WHERE
    EXISTS( SELECT 
            *
        FROM
            dept_manager dm
        WHERE
            dm.emp_no = e.emp_no);
```

An example of a subquery nested in the from clause in the select statement:

```sql
-- Example from the Employees Database
SELECT 
    a.*
FROM
    (SELECT 
        e.emp_no AS employee_ID,
            MIN(de.dept_no) AS department_code,
            (SELECT 
                    emp_no
                FROM
                    dept_manager
                WHERE
                    emp_no = 110022) AS manager_ID
    FROM
        employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    WHERE
        e.emp_no <= 10020
    GROUP BY e.emp_no
    ORDER BY e.emp_no) AS a;
```