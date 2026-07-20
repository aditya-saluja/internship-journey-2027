SELECT name, salary, (salary + bonus) AS total_salary
FROM employees;



SELECT name,
       salary,
       (salary * 1.10) AS increased_salary
FROM employees;


SELECT name,
       salary,
       bonus,
       (salary + bonus) AS total_income
FROM employees;


SELECT name,
       salary,
       (salary * 2) AS new_salary
FROM employees;
