SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
#数据库数据计算是从0开始的
#offset X是跳过X个数据
#limit Y是选取Y个数据