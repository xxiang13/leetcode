/*
Write a SQL query to rank scores. If there is a tie between two scores, 
both should have the same ranking. Note that after a tie, the next ranking number 
should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report 
(order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/


/* Method 1 */
# Alternative (from kamyu)
 SELECT Score,  (SELECT COUNT(DISTINCT(Score))
 	             FROM  Scores b
 	             WHERE b.Score > a.Score) + 1 AS Rank
FROM Scores a
ORDER by Score DESC


/* Method 2*/
-- in postgreSQL, use DENSE_RANK()
-- reference link: https://blog.jooq.org/2014/08/12/the-difference-between-row_number-rank-and-dense_rank/

SELECT Score, 
  	   DENSE_RANK() OVER(ORDER BY Score desc) as Rank
FROM Scores
ORDER BY 2 desc