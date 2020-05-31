-- https://leetcode.com/problems/consecutive-available-seats/

"""

Several friends at a cinema ticket office would like to reserve consecutive available seats.
Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
 

Your query should return the following result for the sample case above.
 

| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
Note:
The seat_id is an auto increment int, and free is bool ('1' means free, and '0' means occupied.).
Consecutive available seats are more than 2(inclusive) seats consecutively available.

"""

select distinct a.seat_id
from cinema a, cinema b
where a.free = 1 
and b.free =1 
and (a.seat_id + 1 = b.seat_id
or b.seat_id + 1 = a.seat_id)
order by seat_id;


SELECT  c1.seat_id
FROM    cinema c1
WHERE   c1.free = 1 
    AND EXISTS (
        SELECT *
        FROM   cinema c2
        WHERE  (c1.seat_id = c2.seat_id - 1
            OR  c1.seat_id = c2.seat_id + 1)
            AND c2.free = 1
        )
ORDER BY c1.seat_id;

