# Write your MySQL query statement below
#ranking the score 178 
select score, DENSE_RANK() over (order by score desc) as "rank"
from Scores 
order by score desc;