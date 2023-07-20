---
layout: archive
title: "The ON DELETE CASCADE constraint"
permalink: /code/The_ON_DELETE_CASCADE_constraint
author_profile: true
redirect_from: The_ON_DELETE_CASCADE_constraint
---

`ON DELETE CASCADE` constraint is used in MySQL to delete the rows from the child table automatically, when the rows from the parent table are deleted.

For example when a student registers in an online learning platform, then all the details of the student are recorded with their unique number/id. All the courses in these online learning platforms had their own code, title, and name. Students can enroll in any course according to their wishes. 

There is no rule that all students must enroll in all courses, or they have to join the course on the same date. A student can enroll in one or more courses.

Suppose you delete a row from the “Student” table, now you will also want to delete all rows in the “Enroll” table that references the row in the “Student” table. For that, we need `ON DELETE CASCADE`.

#### Example of use: [[The FOREIGN KEY constraint]]
