/* 

The Employee table holds all employees including their managers. Every employee has an Id, 
and there is also a column for the manager Id.
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. 
For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

*/



/* Try 1: 

Wrong answer under condition more than one employees has a same manager
Sub-table b would generate repetitive manager rows, so final output would be repetitive employee
Exmaple table: 
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Mark  | 40000  | 2         |
| 3  | Jack  | 30000  | 2         |
| 2  | Ala   | 20000  | NULL      |
+----+-------+--------+-----------+

*/

select a.Name as Employee
from Employee a, 
(select c.ID as ID, c.Salary as Salary from Employee c, Employee d 
	where c.ID = d.ManagerID and d.ManagerID is not NULL) b
where a.Salary > b.Salary and a.ManagerID != NULL and a.ManagerID = b.ID;


-- Try 2: Correct one
select d.Name as ID from Employee c, Employee d 
	where c.ID = d.ManagerID and d.Salary > c.Salary;
