---
layout: archive
title: "SQL Numeric Data Type & Functions"
permalink: /code/SQL_Numeric_Data_Type_&_Functions
author_profile: true
redirect_from: SQL_Numeric_Data_Type_&_Functions
---
# Numeric Data Types
**Data type - Description**                             

`BIT(_size_)` - A bit-value type. The number of bits per value is specified in _size_. The _size_ parameter can hold a value from 1 to 64. The default value for _size_ is 1.

`TINYINT(_size_)` - A very small integer. Signed range is from -128 to 127. Unsigned range is from 0 to 255. The _size_ parameter specifies the maximum display width (which is 255)

`BOOL` - Zero is considered as false, nonzero values are considered as true.

`BOOLEAN` - Equal to BOOL

`SMALLINT(_size_)` - A small integer. Signed range is from -32768 to 32767. Unsigned range is from 0 to 65535. The _size_ parameter specifies the maximum display width (which is 255)

`MEDIUMINT(_size_)` - A medium integer. Signed range is from -8388608 to 8388607. Unsigned range is from 0 to 16777215. The _size_ parameter specifies the maximum display width (which is 255)

`INT(_size_)` - A medium integer. Signed range is from -2147483648 to 2147483647. Unsigned range is from 0 to 4294967295. The _size_ parameter specifies the maximum display width (which is 255)

`INTEGER(_size_)` - Equal to INT(size)

`BIGINT(_size_)` - A large integer. Signed range is from -9223372036854775808 to 9223372036854775807. Unsigned range is from 0 to 18446744073709551615. The _size_ parameter specifies the maximum display width (which is 255)

`FLOAT(_size_, _d_)` - A floating point number. The total number of digits is specified in _size_. The number of digits after the decimal point is specified in the _d_ parameter. This syntax is deprecated in MySQL 8.0.17, and it will be removed in future MySQL versions

`FLOAT(_p_)` - A floating point number. MySQL uses the _p_ value to determine whether to use FLOAT or DOUBLE for the resulting data type. If _p_ is from 0 to 24, the data type becomes FLOAT(). If _p_ is from 25 to 53, the data type becomes DOUBLE()

`DOUBLE(_size_, _d_)` - A normal-size floating point number. The total number of digits is specified in _size_. The number of digits after the decimal point is specified in the _d_ parameter

`DECIMAL(_size_, _d_)` - An exact fixed-point number. The total number of digits is specified in _size_. The number of digits after the decimal point is specified in the _d_ parameter. The maximum number for _size_ is 65. The maximum number for _d_ is 30. The default value for _size_ is 10. The default value for _d_ is 0.

`DEC(_size_, _d_)` - Equal to DECIMAL(size,d)


**Function - Description**

[ABS](https://www.w3schools.com/sql/func_mysql_abs.asp) - Returns the absolute value of a number

[ACOS](https://www.w3schools.com/sql/func_mysql_acos.asp) - Returns the arc cosine of a number

[ASIN](https://www.w3schools.com/sql/func_mysql_asin.asp) - Returns the arc sine of a number

[ATAN](https://www.w3schools.com/sql/func_mysql_atan.asp) - Returns the arc tangent of one or two numbers

[ATAN2](https://www.w3schools.com/sql/func_mysql_atan2.asp) - Returns the arc tangent of two numbers

[AVG](https://www.w3schools.com/sql/func_mysql_avg.asp) - Returns the average value of an expression

[CEIL](https://www.w3schools.com/sql/func_mysql_ceil.asp) - Returns the smallest integer value that is >= to a number

[CEILING](https://www.w3schools.com/sql/func_mysql_ceiling.asp) - Returns the smallest integer value that is >= to a number

[COS](https://www.w3schools.com/sql/func_mysql_cos.asp) - Returns the cosine of a number

[COT](https://www.w3schools.com/sql/func_mysql_cot.asp) - Returns the cotangent of a number

[COUNT](https://www.w3schools.com/sql/func_mysql_count.asp) - Returns the number of records returned by a select query

[DEGREES](https://www.w3schools.com/sql/func_mysql_degrees.asp) - Converts a value in radians to degrees

[DIV](https://www.w3schools.com/sql/func_mysql_div.asp) - Used for integer division

[EXP](https://www.w3schools.com/sql/func_mysql_exp.asp) - Returns e raised to the power of a specified number

[FLOOR](https://www.w3schools.com/sql/func_mysql_floor.asp) - Returns the largest integer value that is <= to a number

[GREATEST](https://www.w3schools.com/sql/func_mysql_greatest.asp) - Returns the greatest value of the list of arguments

[LEAST](https://www.w3schools.com/sql/func_mysql_least.asp) - Returns the smallest value of the list of arguments

[LN](https://www.w3schools.com/sql/func_mysql_ln.asp) - Returns the natural logarithm of a number

[LOG](https://www.w3schools.com/sql/func_mysql_log.asp) - Returns the natural logarithm of a number, or the logarithm of a number to a specified base

[LOG10](https://www.w3schools.com/sql/func_mysql_log10.asp) - Returns the natural logarithm of a number to base 10

[LOG2](https://www.w3schools.com/sql/func_mysql_log2.asp) - Returns the natural logarithm of a number to base 2

[MAX](https://www.w3schools.com/sql/func_mysql_max.asp) - Returns the maximum value in a set of values

[MIN](https://www.w3schools.com/sql/func_mysql_min.asp) - Returns the minimum value in a set of values

[MOD](https://www.w3schools.com/sql/func_mysql_mod.asp) - Returns the remainder of a number divided by another number

[PI](https://www.w3schools.com/sql/func_mysql_pi.asp) - Returns the value of PI

[POW](https://www.w3schools.com/sql/func_mysql_pow.asp) - Returns the value of a number raised to the power of another number

[POWER](https://www.w3schools.com/sql/func_mysql_power.asp) - Returns the value of a number raised to the power of another number

[RADIANS](https://www.w3schools.com/sql/func_mysql_radians.asp) - Converts a degree value into radians

[RAND](https://www.w3schools.com/sql/func_mysql_rand.asp) - Returns a random number

[ROUND](https://www.w3schools.com/sql/func_mysql_round.asp) - Rounds a number to a specified number of decimal places

[SIGN](https://www.w3schools.com/sql/func_mysql_sign.asp) - Returns the sign of a number

[SIN](https://www.w3schools.com/sql/func_mysql_sin.asp) - Returns the sine of a number

[SQRT](https://www.w3schools.com/sql/func_mysql_sqrt.asp) - Returns the square root of a number

[SUM](https://www.w3schools.com/sql/func_mysql_sum.asp) - Calculates the sum of a set of values

[TAN](https://www.w3schools.com/sql/func_mysql_tan.asp) - Returns the tangent of a number

[TRUNCATE](https://www.w3schools.com/sql/func_mysql_truncate.asp) - Truncates a number to the specified number of decimal places