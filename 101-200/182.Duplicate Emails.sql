# Write your MySQL query statement below
select email
from person
group by email
having count(email)>1
#group by .... having ...(用于分组后)