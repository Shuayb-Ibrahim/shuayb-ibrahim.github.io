# The CASE statement
Control statements form the heart of most languages since they control the execution of other sets of statements. These are found in SQL too as Case-Switch statements.
The `CASE` statement is SQL's way of handling if/then logic. The `CASE` statement is followed by at least one pair of `WHEN` and `THEN` statements—SQL's equivalent of IF/THEN in Excel. Because of this pairing, you might be tempted to call this SQL `CASE WHEN`, but `CASE` is the accepted term.

Every `CASE` statement must end with the `END` statement. The `ELSE` statement is optional, and provides a way to capture values not specified in the `WHEN`/`THEN` statements.

<u>The syntax for the `CASE` statement:</u>
```sql
CASE  
 WHEN _condition1_ THEN _result1_  
 WHEN _condition2_ THEN _result2_  
 WHEN _conditionN_ THEN _resultN_  
 ELSE _result_  
END AS column_name;
```

You can also string together multiple conditional statements with `AND` and `OR` the same way you might in a `WHERE` clause:
```sql
CASE  
 WHEN _condition1_ AND _condition2_ THEN _result1_  
 WHEN _condition3_ OR _condition4_ THEN _result2_  
 ELSE _result_  
END AS column_name;
```

#### Using the CASE statement with aggregate functions
`CASE`'s slightly more complicated and substantially more useful functionality comes from pairing it with [[SQL Aggregate Functions]]. For example, let's say you want to only count rows that fulfil a certain condition. Since [[The COUNT() function]] ignores nulls, you could use a `CASE` statement to evaluate the condition and produce null or non-null values depending on the outcome:
```sql
SELECT CASE
 WHEN _condition1_ THEN _result1_ -- e.g. condition being column_name = 'NA' 
 ELSE _not_result1_,
 COUNT(*) AS count
 END AS column_name
FROM table_name
GROUP BY CASE
 WHEN _condition1_ THEN _result1_
 ELSE _not_result1_
 END;
```

