# Write your MySQL query statement below
update salary
set sex=char(ASCII('f')^ASCII('m')^ASCII(sex))