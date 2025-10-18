-- ===================================
-- PART II — Many-to-Many: Books / Students / Library
-- ===================================

DROP TABLE IF EXISTS library CASCADE;
DROP TABLE IF EXISTS student CASCADE;
DROP TABLE IF EXISTS book CASCADE;

-- Books
CREATE TABLE book (
  book_id SERIAL PRIMARY KEY,
  title   TEXT NOT NULL,
  author  TEXT NOT NULL
);

INSERT INTO book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- Students (age <= 15 enforced)
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

-- Junction table (Many-to-Many)
CREATE TABLE library (
  book_fk_id    INT NOT NULL,
  student_fk_id INT NOT NULL,
  borrowed_date DATE NOT NULL,
  PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date),
  FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert using subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES
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

-- === Queries ===

-- 1️⃣ Select all columns
SELECT * FROM library ORDER BY borrowed_date;

-- 2️⃣ Student names and book titles
SELECT s.name AS student, b.title AS book, l.borrowed_date
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book b ON b.book_id = l.book_fk_id
ORDER BY s.name, l.borrowed_date;

-- 3️⃣ Average age of children who borrowed "Alice In Wonderland"
SELECT ROUND(AVG(s.age),2) AS avg_age_alice
FROM library l
JOIN student s ON s.student_id = l.student_fk_id
JOIN book b ON b.book_id = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

-- 4️⃣ Test cascade: delete Bob
DELETE FROM student WHERE name = 'Bob';

-- Show remaining data
SELECT * FROM library ORDER BY borrowed_date;