select employer.Name as employee
#"as"将表的列重命名
from  Employee employer join Employee manager on (employer.ManagerId = manager.Id )
where employer.Salary > manager.Salary ;