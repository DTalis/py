------------------------------------------------------------
-- 1. Create the employees table and insert sample data
------------------------------------------------------------

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

------------------------------------------------------------
-- 2. Identify and handle missing values
------------------------------------------------------------

-- Check for NULLs or empty strings
SELECT * FROM employees
WHERE department IS NULL OR TRIM(department) = '';

-- Option 1: Replace missing department with 'Unknown'
UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL OR TRIM(department) = '';

------------------------------------------------------------
-- 3. Check and remove duplicate rows
------------------------------------------------------------

-- Check for duplicates by all columns
SELECT employee_name, salary, hire_date, department, COUNT(*)
FROM employees
GROUP BY employee_name, salary, hire_date, department
HAVING COUNT(*) > 1;

-- Remove duplicates (keeping the smallest employee_id)
DELETE FROM employees a
USING employees b
WHERE a.employee_id > b.employee_id
  AND a.employee_name = b.employee_name
  AND a.salary = b.salary
  AND a.hire_date = b.hire_date
  AND a.department = b.department;

------------------------------------------------------------
-- 4. Correct structural issues and inconsistent names
------------------------------------------------------------

-- Capitalize names properly and trim spaces
UPDATE employees
SET employee_name = INITCAP(TRIM(employee_name));

-- Standardize department names (capitalize properly)
UPDATE employees
SET department = INITCAP(TRIM(department));

------------------------------------------------------------
-- 5. Ensure correct data types (convert hire_date to DATE)
------------------------------------------------------------

-- Add a temporary date column
ALTER TABLE employees ADD COLUMN hire_date_clean DATE;

UPDATE employees
SET hire_date_clean = TO_DATE(hire_date, 'YYYY-MM-DD');

-- Drop old column and rename new one
ALTER TABLE employees DROP COLUMN hire_date;
ALTER TABLE employees RENAME COLUMN hire_date_clean TO hire_date;

------------------------------------------------------------
-- 6. Detect outliers in salary
------------------------------------------------------------

-- Calculate salary stats
SELECT 
  MIN(salary) AS min_salary,
  MAX(salary) AS max_salary,
  ROUND(AVG(salary),2) AS avg_salary,
  ROUND(STDDEV(salary),2) AS stddev_salary
FROM employees;

-- Identify potential outliers (3 standard deviations rule)
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) + 3 * STDDEV(salary) FROM employees)
   OR salary < (SELECT AVG(salary) - 3 * STDDEV(salary) FROM employees);

------------------------------------------------------------
-- 7. Standardize data — e.g., normalized salary range (0–1)
------------------------------------------------------------

-- Add normalized salary column
ALTER TABLE employees ADD COLUMN salary_normalized NUMERIC;

UPDATE employees
SET salary_normalized = ROUND(
  (salary - (SELECT MIN(salary) FROM employees)) /
  ((SELECT MAX(salary) FROM employees) - (SELECT MIN(salary) FROM employees)),
  3
);

------------------------------------------------------------
-- 8. Final check — cleaned dataset
------------------------------------------------------------

SELECT * FROM employees ORDER BY employee_id;