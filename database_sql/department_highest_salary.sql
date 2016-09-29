/*
The Employee table holds all employees. Every employee has an Id, a salary, 
and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of 
the departments. For the above tables, Max has the highest salary in the 
IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
*/

/* Method 1*/
select D.Name Department, E.Name Employee, A.Salary
from Employee E, Department D,
(select DepartmentId, max(salary) salary from Employee group by DepartmentId) A
where E.DepartmentId = D.Id and A.DepartmentId = D.Id
and E.Salary = A.salary;


/* Method 2*/
-- use correlative sub query to get highest salary for corresponding department

select D.Name as Department, E.Name as Employee, E.Salary as Salary
from Employee E
inner join Department D on E.DepartmentId=D.Id
where salary = (select max(salary) from Employee where DepartmentId=E.DepartmentId)