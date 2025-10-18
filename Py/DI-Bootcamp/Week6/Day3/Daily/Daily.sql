DROP TABLE IF EXISTS library CASCADE;
DROP TABLE IF EXISTS student CASCADE;
DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS customer_profile CASCADE;
DROP TABLE IF EXISTS customer CASCADE;

-- PART I — One-to-One: Customer/Profile

CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name  TEXT NOT NULL
);

CREATE TABLE customer_profile (
  id SERIAL PRIMARY KEY,
  isloggedin BOOLEAN NOT NULL DEFAULT FALSE,
  customer_id INT UNIQUE REFERENCES customer(id) ON DELETE CASCADE ON UPDATE CASCADE
  -- UNIQUE ensures "only one profile per customer"
);

-- Insert customers
INSERT INTO customer (first_name, last_name) VALUES
('John','Doe'),
('Jerome','Lalu'),
('Lea','Rive');

-- Insert profiles using subqueries
-- John is logged in
INSERT INTO customer_profile (isloggedin, customer_id)
VALUES (
  TRUE,
  (SELECT id FROM customer WHERE first_name='John' AND last_name='Doe')
);

-- Jerome is NOT logged in (explicit FALSE for clarity)
INSERT INTO customer_profile (isloggedin, customer_id)
VALUES (
  FALSE,
  (SELECT id FROM customer WHERE first_name='Jerome' AND last_name='Lalu')
);

-- ===== Required displays (JOINs) =====

-- 1) First names of logged-in customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON cp.customer_id = c.id
WHERE cp.isloggedin = TRUE;

-- 2) All customers' first_name + isLoggedIn, including those without a profile
SELECT
  c.first_name,
  COALESCE(cp.isloggedin, FALSE) AS isloggedin, -- or leave as NULL if you want “no profile”
  CASE WHEN cp.id IS NULL THEN 'no profile' ELSE 'has profile' END AS profile_status
FROM customer c
LEFT JOIN customer_profile cp ON cp.customer_id = c.id
ORDER BY c.id;

-- 3) Number of customers that are NOT logged in
-- (Interpretation: either have a profile marked FALSE OR have no profile at all.)
SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp ON cp.customer_id = c.id
WHERE COALESCE(cp.isloggedin, FALSE) = FALSE;

-- PART II — Many-to-Many: Books / Students via Library

CREATE TABLE book (
  book_id SERIAL PRIMARY KEY,
  title   TEXT NOT NULL,
  author  TEXT NOT NULL
);

INSERT INTO book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- Students: age must never be > 15
CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  age  INT  NOT NULL,
  CONSTRAINT chk_age_le_15 CHECK (age <= 15)
);

INSERT INTO student (name, age) VALUES
('John',    12),
('Lera',    11),
('Patrick', 10),
('Bob',     14);

-- Junction table with composite PK and cascading FKs
CREATE TABLE library (
  book_fk_id    INT NOT NULL,
  student_fk_id INT NOT NULL,
  borrowed_date DATE NOT NULL,
  PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date), -- allow same student/book on different dates
  FOREIGN KEY (book_fk_id)    REFERENCES book(book_id)       ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (student_fk_id) REFERENCES student(student_id)  ON DELETE CASCADE ON UPDATE CASCADE
);

-- Add 4 records using subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date) VALUES
(
  (SELECT book_id FROM book WHERE title='Alice In Wonderland'),
  (SELECT student_id FROM student WHERE name='John'),
  DATE '2022-02-15'
),
(
  (SELECT book_id FROM book WHERE title='To kill a mockingbird'),
  (SELECT student_id FROM student WHERE name='Bob'),
  DATE '2021-03-03'
),
(
  (SELECT book_id FROM book WHERE title='Alice In Wonderland'),
  (SELECT student_id FROM student WHERE name='Lera'),
  DATE '2021-05-23'
),
(
  (SELECT book_id FROM book WHERE title='Harry Potter'),
  (SELECT student_id FROM student WHERE name='Bob'),
  DATE '2021-08-12'
);

-- ===== Displays / Queries =====

-- A) Select all columns from the junction table
SELECT * FROM library ORDER BY borrowed_date;

-- B) Select the student name and the title of the borrowed books
SELECT s.name AS student, b.title AS book, l.borrowed_date
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book    b ON b.book_id    = l.book_fk_id
ORDER BY s.name, l.borrowed_date;

-- C) Average age of children who borrowed "Alice In Wonderland"
SELECT AVG(s.age)::NUMERIC(4,2) AS avg_age_alice
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book    b ON b.book_id    = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

-- D) Delete a student and observe the cascade in the junction table
-- Example: delete Bob, then re-check the library table
DELETE FROM student WHERE name = 'Bob';

-- Show the current library rows after delete to see cascaded removals
SELECT * FROM library ORDER BY borrowed_date;