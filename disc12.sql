Our tables:
records: Name Division Title Salary Supervisor

2.1 Write a query that outputs the names of employees that Oliver Warbucks directly
supervises.

SELECT Name FROM records WHERE Supervisor = 'Oliver Warbucks';

2.2 Write a query that outputs all information about employees that supervise themselves.

SELECT * FROM records WHERE Supervisor = Name;

2.3 Write a query that outputs the names of all employees with salary greater than
50,000 in alphabetical order.

SELECT Name FROM records WHERE Salary > 50000 ORDER BY Name;


Our tables:
records: Name Division Title Salary Supervisor

meetings: Division Day Time

3.1 Write a query that outputs the meeting days and times of all employees directly
supervised by Oliver Warbucks.

SELECT b.day, b.time FROM records AS a, meetings AS b 
    WHERE a.division = b.division AND a.supervise = ' Oliver Warbucks'; 

3.2 Write a query that outputs the names of all pairs of employees that have a meeting
at the same time. Make sure that if A|B appears in your output, B|A does not
appear as well (A|A and B|B should additionally not appear).

SELECT e1.name, e2.name FROM records as e1, records as e2, meetings as m1, meetings as m2
WHERE e1.division = m1.division AND e2.division = m2.division AND
m1.time = m2.time AND AND m1.day = m2.day AND
e1.name < e2.name;

3.3 (Extra question) Will the statement above filter out all redundant output in all
cases? Why or why not?



3.4 Write a query that outputs the names of employees whose supervisor is in a different
division.
SELECT r.name FROM records AS r, records AS s
 WHERE r.supervisor = s.name AND r.division != s.division;


4.1
SELECT supervisor, sum(salary) FROM records GROUP BY supervisor;

4.2
SELECT m.day FROM meetings AS m, records AS r
 WHERE m.division = r.division GROUP BY m.day HAVING COUNT(*) < 5;

 5.2
 CREATE TABLE num_taught AS 
  SELECT professor AS professor, courese AS courese, COUNT(*) AS times FROM num_taught
   GROUP BY professor,courese;

5.3
SELECT a.professor, b.professor, a.courese FROM num_taught AS a, num_taught AS b
 WHERE a.courese = b.courese AND a.times = b.times AND a.professor > b.professor;

5.4
SELECT a.professor, b.professor FROM courese AS a, courese AS b
 WHERE a.professor > b.professor AND a.semester = b.semester AND a.courese = b.courese
  GROUP BY a.courese, a.professor, b.professor HAVING COUNT(*) > 1; 
  