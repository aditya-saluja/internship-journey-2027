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