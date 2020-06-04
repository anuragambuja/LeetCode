-- https://leetcode.com/problems/reformat-department-table/

"""
Table: Department

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The query result format is in the following example:

Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Note that the result table has 13 columns (1 for the department id + 12 for the months).

"""

select id, max(case when month = 'Jan' then revenue end) as Jan_Revenue,
max(case when month = 'Feb' then revenue end) as Feb_Revenue,
max(case when month = 'Mar' then revenue end) as Mar_Revenue,
max(case when month = 'Apr' then revenue end) as Apr_Revenue,
max(case when month = 'May' then revenue end) as May_Revenue,
max(case when month = 'Jun' then revenue end) as Jun_Revenue,
max(case when month = 'Jul' then revenue end) as Jul_Revenue,
max(case when month = 'Aug' then revenue end) as Aug_Revenue,
max(case when month = 'Sep' then revenue end) as Sep_Revenue,
max(case when month = 'Oct' then revenue end) as Oct_Revenue,
max(case when month = 'Nov' then revenue end) as Nov_Revenue,
max(case when month = 'Dec' then revenue end) as Dec_Revenue

from Department
group by id


Select id
,'Jan' as Jan_revenue
,'Feb' as Feb_revenue
,'Mar' as Mar_revenue
,'Apr' as Apr_revenue
,'May' as May_revenue
,'Jun' as Jun_revenue
,'Jul' as Jul_revenue
,'Aug' as Aug_revenue
,'Sep' as Sep_revenue
,'Oct' as Oct_revenue
,'Nov' as Nov_revenue
,'Dec' as Dec_revenue
from
( Select id, revenue, month
from Department
)
PIVOT
(
SUM(revenue)
for month in ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
) 


SELECT * FROM
(
SELECT *
FROM Department
)
PIVOT
(
Sum(revenue)
FOR Month IN ('Jan' as "Jan_Revenue" ,'Feb' as "Feb_Revenue", 'Mar' as "Mar_Revenue",'Apr' as "Apr_Revenue"
, 'May' as "May_Revenue",'Jun' as "Jun_Revenue",'Jul' as "Jul_Revenue",'Aug' as "Aug_Revenue"
,'Sep' as "Sep_Revenue",'Oct' as "Oct_Revenue",'Nov' as "Nov_Revenue",'Dec' as "Dec_Revenue")
)
ORDER BY id


