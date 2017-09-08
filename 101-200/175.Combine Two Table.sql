select FirstName,LastName,City,State
from Person
left join Address
on Person.PersonId=Address.PersonId
#LEFT JOIN 关键字会从
#左表#(table_name1) 那里返回所有的行
#即使在右表 (table_name2) 中没有匹配的行。