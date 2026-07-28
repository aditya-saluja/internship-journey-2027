-- PROBLEM 175
-- COMBINE TABLES


SELECT person.firstName, address.city
FROM person
LEFT JOIN address
ON person.personId = address.personId


-- 181
-- SELF JOIN 

SELECT e.name AS employee
FROM employee e
JOIN employee m 
ON e.managerId = m.id 
WHERE e.salary > m.salary

-- GROUP BY / HAVING

SELECT email FROM person
GROUP BY email 
HAVING COUNT(*) > 1


-- PROBLEM 196
SELECT email FROM person
GROUP BY email 
HAVING COUNT(*) < 2
WHERE SAME email > id


--  1661

SELECT A.machine_id,
ROUND(AVG(M.timestamp - A.timestamp), 3) AS processing_time

FROM activty AS A 
INNER JOIN activity AS M 
ON A.machine_id = M.machine_id
AND A.process_id = M.process_id
AND A.process_id = "start"
AND M.process_id = "end"
GROUP BY A.machine_id


-- 620
SELECT *
FROM movies AS M     
WHERE id % 2 = 1 AND description != "boring"
ORDER BY rating DESC

