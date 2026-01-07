# Write your MySQL query statement below
select w.id 
from Weather w
join Weather w2 
where SUBDATE(w.recordDate, 1) = w2. recordDate and w.temperature > w2.temperature;