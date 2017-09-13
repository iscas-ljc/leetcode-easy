# Write your MySQL query statement below
select a.name as customers
from customers a
where  a.id not in (select b.customerid from orders b)