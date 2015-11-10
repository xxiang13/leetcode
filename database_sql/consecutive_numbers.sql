/*
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively 
for at least three times.
*/

select distinct A.Num as ConsecutiveNums
from Logs A inner join Logs B
on A.ID+ 1= B.ID and A.Num = B.Num
inner join Logs C 
on B.ID+1 = C.ID and B.Num = C.Num;


