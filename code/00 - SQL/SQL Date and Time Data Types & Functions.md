# Date and Time Data Types
**Data Type - Description**

`DATE` - A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'

`DATETIME(_fsp_)` - A date and time combination. Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'. Adding DEFAULT and ON UPDATE in the column definition to get automatic initialization and updating to the current date and time

`TIMESTAMP(_fsp_)` - A timestamp. TIMESTAMP values are stored as the number of seconds since the Unix epoch ('1970-01-01 00:00:00' UTC). Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1970-01-01 00:00:01' UTC to '2038-01-09 03:14:07' UTC. Automatic initialization and updating to the current date and time can be specified using DEFAULT CURRENT_TIMESTAMP and ON UPDATE CURRENT_TIMESTAMP in the column definition

`TIME(_fsp_)` - A time. Format: hh:mm:ss. The supported range is from '-838:59:59' to '838:59:59'

`YEAR` - A year in four-digit format. Values allowed in four-digit format: 1901 to 2155, and 0000.  


**Function - Description**

[ADDDATE](https://www.w3schools.com/sql/func_mysql_adddate.asp) - Adds a time/date interval to a date and then returns the date

[ADDTIME](https://www.w3schools.com/sql/func_mysql_addtime.asp) - Adds a time interval to a time/datetime and then returns the time/datetime

[CURDATE](https://www.w3schools.com/sql/func_mysql_curdate.asp) - Returns the current date

[CURRENT_DATE](https://www.w3schools.com/sql/func_mysql_current_date.asp) - Returns the current date

[CURRENT_TIME](https://www.w3schools.com/sql/func_mysql_current_time.asp) - Returns the current time

[CURRENT_TIMESTAMP](https://www.w3schools.com/sql/func_mysql_current_timestamp.asp) - Returns the current date and time

[CURTIME](https://www.w3schools.com/sql/func_mysql_curtime.asp) - Returns the current time

[DATE](https://www.w3schools.com/sql/func_mysql_date.asp) - Extracts the date part from a datetime expression

[DATEDIFF](https://www.w3schools.com/sql/func_mysql_datediff.asp) - Returns the number of days between two date values

[DATE_ADD](https://www.w3schools.com/sql/func_mysql_date_add.asp) - Adds a time/date interval to a date and then returns the date

[DATE_FORMAT](https://www.w3schools.com/sql/func_mysql_date_format.asp) - Formats a date

[DATE_SUB](https://www.w3schools.com/sql/func_mysql_date_sub.asp) - Subtracts a time/date interval from a date and then returns the date

[DAY](https://www.w3schools.com/sql/func_mysql_day.asp) - Returns the day of the month for a given date

[DAYNAME](https://www.w3schools.com/sql/func_mysql_dayname.asp) - Returns the weekday name for a given date

[DAYOFMONTH](https://www.w3schools.com/sql/func_mysql_dayofmonth.asp) - Returns the day of the month for a given date

[DAYOFWEEK](https://www.w3schools.com/sql/func_mysql_dayofweek.asp) - Returns the weekday index for a given date

[DAYOFYEAR](https://www.w3schools.com/sql/func_mysql_dayofyear.asp) - Returns the day of the year for a given date

[EXTRACT](https://www.w3schools.com/sql/func_mysql_extract.asp) - Extracts a part from a given date

[FROM_DAYS](https://www.w3schools.com/sql/func_mysql_from_days.asp) - Returns a date from a numeric date value

[HOUR](https://www.w3schools.com/sql/func_mysql_hour.asp) - Returns the hour part for a given date

[LAST_DAY](https://www.w3schools.com/sql/func_mysql_last_day.asp) - Extracts the last day of the month for a given date

[LOCALTIME](https://www.w3schools.com/sql/func_mysql_localtime.asp) - Returns the current date and time

[LOCALTIMESTAMP](https://www.w3schools.com/sql/func_mysql_localtimestamp.asp) - Returns the current date and time

[MAKEDATE](https://www.w3schools.com/sql/func_mysql_makedate.asp) - Creates and returns a date based on a year and a number of days value

[MAKETIME](https://www.w3schools.com/sql/func_mysql_maketime.asp) - Creates and returns a time based on an hour, minute, and second value

[MICROSECOND](https://www.w3schools.com/sql/func_mysql_microsecond.asp) - Returns the microsecond part of a time/datetime

[MINUTE](https://www.w3schools.com/sql/func_mysql_minute.asp) - Returns the minute part of a time/datetime

[MONTH](https://www.w3schools.com/sql/func_mysql_month.asp) - Returns the month part for a given date

[MONTHNAME](https://www.w3schools.com/sql/func_mysql_monthname.asp) - Returns the name of the month for a given date

[NOW](https://www.w3schools.com/sql/func_mysql_now.asp) - Returns the current date and time

[PERIOD_ADD](https://www.w3schools.com/sql/func_mysql_period_add.asp) - Adds a specified number of months to a period

[PERIOD_DIFF](https://www.w3schools.com/sql/func_mysql_period_diff.asp) - Returns the difference between two periods

[QUARTER](https://www.w3schools.com/sql/func_mysql_quarter.asp) - Returns the quarter of the year for a given date value

[SECOND](https://www.w3schools.com/sql/func_mysql_second.asp) - Returns the seconds part of a time/datetime

[SEC_TO_TIME](https://www.w3schools.com/sql/func_mysql_sec_to_time.asp) - Returns a time value based on the specified seconds

[STR_TO_DATE](https://www.w3schools.com/sql/func_mysql_str_to_date.asp) - Returns a date based on a string and a format

[SUBDATE](https://www.w3schools.com/sql/func_mysql_subdate.asp) - Subtracts a time/date interval from a date and then returns the date

[SUBTIME](https://www.w3schools.com/sql/func_mysql_subtime.asp) - Subtracts a time interval from a datetime and then returns the time/datetime

[SYSDATE](https://www.w3schools.com/sql/func_mysql_sysdate.asp) - Returns the current date and time

[TIME](https://www.w3schools.com/sql/func_mysql_time.asp) - Extracts the time part from a given time/datetime

[TIME_FORMAT](https://www.w3schools.com/sql/func_mysql_time_format.asp) - Formats a time by a specified format

[TIME_TO_SEC](https://www.w3schools.com/sql/func_mysql_time_to_sec.asp) - Converts a time value into seconds

[TIMEDIFF](https://www.w3schools.com/sql/func_mysql_timediff.asp) - Returns the difference between two time/datetime expressions

[TIMESTAMP](https://www.w3schools.com/sql/func_mysql_timestamp.asp) - Returns a datetime value based on a date or datetime value

[TO_DAYS](https://www.w3schools.com/sql/func_mysql_to_days.asp) - Returns the number of days between a date and date "0000-00-00"

[WEEK](https://www.w3schools.com/sql/func_mysql_week.asp) - Returns the week number for a given date

[WEEKDAY](https://www.w3schools.com/sql/func_mysql_weekday.asp) - Returns the weekday number for a given date

[WEEKOFYEAR](https://www.w3schools.com/sql/func_mysql_weekofyear.asp) - Returns the week number for a given date

[YEAR](https://www.w3schools.com/sql/func_mysql_year.asp) - Returns the year part for a given date

[YEARWEEK](https://www.w3schools.com/sql/func_mysql_yearweek.asp) - Returns the year and week number for a given date