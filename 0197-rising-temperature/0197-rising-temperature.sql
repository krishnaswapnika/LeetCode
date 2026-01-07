# Write your MySQL query statement below
select w.id 
from Weather w
join Weather w2 
on DATEDIFF(w.recordDate, w2.recordDate) = 1 and w.temperature > w2.temperature;