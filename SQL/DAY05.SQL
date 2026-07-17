-- INNER JOIN
-- SYNTAX

SELECT Employees.name, Departments.Department
FROM Employees
RIGHT JOIN Departments
ON Employees.dept_id = Departments.dept_id;



SELECT Employees.name, Departments.Department
FROM Employees
LEFT JOIN Departments
ON Employees.dept_id = Departments.dept_id;


SELECT Employees.name, Departments.Department
FROM Employees
INNER JOIN Departments
ON Employees.dept_id = Departments.dept_id;