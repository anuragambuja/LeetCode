-- https://leetcode.com/problems/consecutive-numbers/

"""

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
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
"""

select distinct a.num  ConsecutiveNums 
from logs a
where num = (select num from logs b where b.id = a.id+1 )
and num = (select num from logs b where b.id = a.id+2 );

