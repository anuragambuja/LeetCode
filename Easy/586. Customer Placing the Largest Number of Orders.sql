-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

"""
Query the customer_number from the orders table for the customer who has placed the largest number of orders.

It is guaranteed that exactly one customer will have placed more orders than any other customer.

The orders table is defined as follows:

| Column            | Type      |
|-------------------|-----------|
| order_number (PK) | int       |
| customer_number   | int       |
| order_date        | date      |
| required_date     | date      |
| shipped_date      | date      |
| status            | char(15)  |
| comment           | char(200) |
Sample Input

| order_number | customer_number | order_date | required_date | shipped_date | status | comment |
|--------------|-----------------|------------|---------------|--------------|--------|---------|
| 1            | 1               | 2017-04-09 | 2017-04-13    | 2017-04-12   | Closed |         |
| 2            | 2               | 2017-04-15 | 2017-04-20    | 2017-04-18   | Closed |         |
| 3            | 3               | 2017-04-16 | 2017-04-25    | 2017-04-20   | Closed |         |
| 4            | 3               | 2017-04-18 | 2017-04-28    | 2017-04-25   | Closed |         |
Sample Output

| customer_number |
|-----------------|
| 3               |
Explanation

The customer with number '3' has two orders, which is greater than either customer '1' or '2' because each of them  only has one order. 
So the result is customer_number '3'.
Follow up: What if more than one customer have the largest number of orders, can you find all the customer_number in this case?

"""

select customer_number
from
(select customer_number, rank() over (order by cnt desc) rnk
from (
select customer_number, count(order_number) cnt 
from orders 
group by customer_number) a ) b
where rnk = 1;


select customer_number
from orders 
group by customer_number
having count(customer_number)= (select max(count(customer_number)) from orders group by customer_number);


select customer_number
from 
(
select customer_number, count(order_number) cnt 
from orders 
group by customer_number
order by cnt desc ) a
where rownum = 1 ;




