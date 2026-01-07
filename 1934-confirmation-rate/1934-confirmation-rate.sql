# Write your MySQL query statement below
# 1934. Confirmation Rate
select  s.user_id, IFNULL(ROUND(sum(action="confirmed")/count(*) , 2), 0.00)  as confirmation_rate
from Signups s
LEFT join  Confirmations c on s.user_id = c.user_id
group by s.user_id