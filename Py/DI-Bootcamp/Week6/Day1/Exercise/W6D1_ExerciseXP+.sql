DROP TABLE IF EXISTS students;

CREATE TABLE students (
id SERIAL PRIMARY KEY,           
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL
);

INSERT INTO students (first_name, last_name, birth_date) 
VALUES('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03'),
('Diana', 'Talis', '1992-05-13');

-- 1) Fetch all data
SELECT * FROM students;

-- 2) Fetch all first_names and last_names
SELECT first_name, last_name FROM students;

-- 3) Fetch student with id = 2
SELECT first_name, last_name FROM students
WHERE id = 2;

-- 4) Student with last_name = 'Benichou' AND first_name = 'Marc'
SELECT first_name, last_name FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- 5) Students with last_name = 'Benichou' OR first_name = 'Marc'
SELECT first_name, last_name FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- 6) Students whose first_names contain 'a' (case-insensitive)
SELECT first_name, last_name FROM students
WHERE first_name ILIKE '%a%';

-- 7) Students whose first_names start with 'a'
SELECT first_name, last_name FROM students
WHERE first_name ILIKE 'a%';

-- 8) Students whose first_names end with 'a'
SELECT first_name, last_name FROM students
WHERE first_name ILIKE '%a';

-- 9) Students whose second-to-last letter is 'a'
SELECT first_name, last_name FROM students
WHERE first_name ILIKE '%a_';

-- 10) Students with ids 1 AND 3 (use IN for clarity)
SELECT first_name, last_name FROM students
WHERE id IN (1, 3);

-- 11) Students born on or after 2000-01-01
SELECT * FROM students
WHERE birth_date >= '2000-01-01';