/*
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to 
its previous (yesterday's) dates.

+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+
For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
*/

-- inner join today (B) with yesterday (a) and todat temp > yesterday temp

select B.Id
from Weather A inner join Weather B
on TO_DAYS(A.date) = TO_DAYS(B.date) - 1
and A.Temperature < B.Temperature;
