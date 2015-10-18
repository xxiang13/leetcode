/*

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

*/


-- Try 1: accepted but too slow
select distinct(a.Email) from Person a, Person b 
where a.ID != b.ID and a.Email = b.Email;

-- Try 2: faster
select Email from Person group by Email having count(Email) > 1;