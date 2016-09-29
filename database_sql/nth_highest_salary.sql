

/*

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200.
 If there is no nth highest salary, then the query should return null.
*/


-- Method 1
# when lim take two argus, 1st one is where to start, 
# 2nd is max number of elements return
# so when max number of elements return larger than available elements.
# it would return NULL
# Here starting from  M = N-1 since the initial row is 0 (not 1)
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
        SELECT DISTINCT Salary FROM Employee ORDER BY Salary 
        DESC LIMIT M,1
  );
END




-- Method 2 from kamyu
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     # Write your MySQL query statement below.
     SELECT MAX(Salary) /*This is the outer query part */
            FROM Employee Emp1
            WHERE (N-1) = ( /* Subquery starts here */
                 SELECT COUNT(DISTINCT(Emp2.Salary))
                        FROM Employee Emp2
                        WHERE Emp2.Salary > Emp1.Salary)
  );
END


