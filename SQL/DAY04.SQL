-- inner join 

SELECT name, subject, marks
FROM students
JOIN marks
ON students.student_id = marks.student_id;