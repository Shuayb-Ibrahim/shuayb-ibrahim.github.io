---
layout: archive
title: "SQL String Data Type & Functions"
permalink: /code/SQL_String_Data_Types_and_Functions
author_profile: true
redirect_from: SQL_String_Data_Types_and_Functions
---

**Data type - Description**                             

`CHAR(size)` - A FIXED length string (can contain letters, numbers, and special characters). The _size_ parameter specifies the column length in characters - can be from 0 to 255. Default is 1

`VARCHAR(size)` - A VARIABLE length string (can contain letters, numbers, and special characters). The _size_ parameter specifies the maximum column length in characters - can be from 0 to 65535

`BINARY(size)` - Equal to CHAR(), but stores binary byte strings. The _size_ parameter specifies the column length in bytes. Default is 1

`VARBINARY(size)` - Equal to VARCHAR(), but stores binary byte strings. The _size_ parameter specifies the maximum column length in bytes.

`TINYBLOB` - For BLOBs (Binary Large Objects). Max length: 255 bytes

`TINYTEXT` - Holds a string with a maximum length of 255 characters

`TEXT(size)` - Holds a string with a maximum length of 65,535 bytes

`BLOB(size)` - For BLOBs (Binary Large Objects). Holds up to 65,535 bytes of data

`MEDIUMTEXT` - Holds a string with a maximum length of 16,777,215 characters

`MEDIUMBLOB` - For BLOBs (Binary Large Objects). Holds up to 16,777,215 bytes of data

`LONGTEXT` - Holds a string with a maximum length of 4,294,967,295 characters

`LONGBLOB` - For BLOBs (Binary Large Objects). Holds up to 4,294,967,295 bytes of data


**Function - Description**                             

[ASCII](https://www.w3schools.com/sql/func_mysql_ascii.asp) - Returns the ASCII value for the specific character

[CHAR_LENGTH](https://www.w3schools.com/sql/func_mysql_char_length.asp) - Returns the length of a string (in characters)

[CHARACTER_LENGTH](https://www.w3schools.com/sql/func_mysql_character_length.asp) - Returns the length of a string (in characters)

[CONCAT](https://www.w3schools.com/sql/func_mysql_concat.asp) - Adds two or more expressions together

[CONCAT_WS](https://www.w3schools.com/sql/func_mysql_concat_ws.asp) - Adds two or more expressions together with a separator

[FIELD](https://www.w3schools.com/sql/func_mysql_field.asp) - Returns the index position of a value in a list of values

[FIND_IN_SET](https://www.w3schools.com/sql/func_mysql_find_in_set.asp) - Returns the position of a string within a list of strings

[FORMAT](https://www.w3schools.com/sql/func_mysql_format.asp) - Formats a number to a format like "#,###,###.##", rounded to a specified number of decimal places

[INSERT](https://www.w3schools.com/sql/func_mysql_insert.asp) - Inserts a string within a string at the specified position and for a certain number of characters

[INSTR](https://www.w3schools.com/sql/func_mysql_instr.asp) - Returns the position of the first occurrence of a string in another string

[LCASE](https://www.w3schools.com/sql/func_mysql_lcase.asp) - Converts a string to lower-case

[LEFT](https://www.w3schools.com/sql/func_mysql_left.asp) - Extracts a number of characters from a string (starting from left)

[LENGTH](https://www.w3schools.com/sql/func_mysql_length.asp) - Returns the length of a string (in bytes)

[LOCATE](https://www.w3schools.com/sql/func_mysql_locate.asp) - Returns the position of the first occurrence of a substring in a string

[LOWER](https://www.w3schools.com/sql/func_mysql_lower.asp) - Converts a string to lower-case

[LPAD](https://www.w3schools.com/sql/func_mysql_lpad.asp) - Left-pads a string with another string, to a certain length

[LTRIM](https://www.w3schools.com/sql/func_mysql_ltrim.asp) - Removes leading spaces from a string

[MID](https://www.w3schools.com/sql/func_mysql_mid.asp) - Extracts a substring from a string (starting at any position)

[POSITION](https://www.w3schools.com/sql/func_mysql_position.asp) - Returns the position of the first occurrence of a substring in a string

[REPEAT](https://www.w3schools.com/sql/func_mysql_repeat.asp) - Repeats a string as many times as specified

[REPLACE](https://www.w3schools.com/sql/func_mysql_replace.asp) - Replaces all occurrences of a substring within a string, with a new substring

[REVERSE](https://www.w3schools.com/sql/func_mysql_reverse.asp) - Reverses a string and returns the result

[RIGHT](https://www.w3schools.com/sql/func_mysql_right.asp) - Extracts a number of characters from a string (starting from right)

[RPAD](https://www.w3schools.com/sql/func_mysql_rpad.asp) - Right-pads a string with another string, to a certain length

[RTRIM](https://www.w3schools.com/sql/func_mysql_rtrim.asp) - Removes trailing spaces from a string

[SPACE](https://www.w3schools.com/sql/func_mysql_space.asp) - Returns a string of the specified number of space characters

[STRCMP](https://www.w3schools.com/sql/func_mysql_strcmp.asp) - Compares two strings

[SUBSTR](https://www.w3schools.com/sql/func_mysql_substr.asp) - Extracts a substring from a string (starting at any position)

[SUBSTRING](https://www.w3schools.com/sql/func_mysql_substring.asp) - Extracts a substring from a string (starting at any position)

[SUBSTRING_INDEX](https://www.w3schools.com/sql/func_mysql_substring_index.asp) - Returns a substring of a string before a specified number of delimiter occurs

[TRIM](https://www.w3schools.com/sql/func_mysql_trim.asp) - Removes leading and trailing spaces from a string

[UCASE](https://www.w3schools.com/sql/func_mysql_ucase.asp) - Converts a string to upper-case

[UPPER](https://www.w3schools.com/sql/func_mysql_upper.asp) - Converts a string to upper-case