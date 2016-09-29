/*
The Employee table holds all employees. Every employee has an Id, and there is also a column
 for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who earn the top three salaries in each of the department.
For the above tables, your SQL query should return the following rows.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
*/


## method 1

# given departmentId, get top 3 salary using correlated subquery

select Salary, DepartmentId
from Employee
where DepartmentId = A.DepartmentId
order by Salary desc limit 3

# check if the salary if in top 3

Salary in (select Salary
			from Employee
			where DepartmentId = E.DepartmentId
			order by Salary desc limit 3)

## final code
# can't test on leetcode, saying mysql version doesn't support limit in subquery

select D.Name as Department, E.Name as Employee, E.Salary as Salary
from
Employee E
inner join Department D 
on E.DepartmentId = D.Id
where Salary in (select distinct Salary
				 from Employee
				 where DepartmentId = E.DepartmentId
				 order by Salary desc limit 3)
Order by Department, Salary desc


## method 2
# count number of Salary larger than the current one,
# Where clause constains to the result with  the number less than 3

select D.Name as Department, E.Name as Employee, E.Salary as Salary 
from Employee E, Department D
where (select COUNT(distinct Salary) from Employee 
       where DepartmentId = E.DepartmentId and Salary > E.Salary) < 3
and E.DepartmentId = D.Id 
order by E.DepartmentId, E.Salary desc

