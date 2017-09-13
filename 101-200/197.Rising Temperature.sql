# Write your MySQL query statement below
select w1.id
from weather w1 , weather w2
where Datediff(w1.date,w2.date)=1 and w1.temperature>w2.temperature
#Datediff返回两个日期格式数据相差日期