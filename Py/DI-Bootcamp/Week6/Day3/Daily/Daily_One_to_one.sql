-- ===================================
-- PART I — One-to-One: Customer / Customer_Profile
-- ===================================

DROP TABLE IF EXISTS customer_profile CASCADE;
DROP TABLE IF EXISTS customer CASCADE;

CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name  TEXT NOT NULL
);

CREATE TABLE customer_profile (
  id SERIAL PRIMARY KEY,
  isloggedin BOOLEAN NOT NULL DEFAULT FALSE,
  customer_id INT UNIQUE REFERENCES customer(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert customers
INSERT INTO customer (first_name, last_name)
VALUES
  ('John','Doe'),
  ('Jerome','Lalu'),
  ('Lea','Rive');

-- Insert customer profiles (using subqueries)
INSERT INTO customer_profile (isloggedin, customer_id)
VALUES
  (TRUE,  (SELECT id FROM customer WHERE first_name='John' AND last_name='Doe')),
  (FALSE, (SELECT id FROM customer WHERE first_name='Jerome' AND last_name='Lalu'));

-- === Required queries ===

-- 1️⃣ First names of logged-in customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isloggedin = TRUE;

-- 2️⃣ All customers (even without a profile)
SELECT
  c.first_name,
  COALESCE(cp.isloggedin, FALSE) AS isloggedin,
  CASE WHEN cp.id IS NULL THEN 'no profile' ELSE 'has profile' END AS profile_status
FROM customer c
LEFT JOIN customer_profile cp ON cp.customer_id = c.id
ORDER BY c.id;

-- 3️⃣ Number of customers that are NOT logged in
SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp ON cp.customer_id = c.id
WHERE COALESCE(cp.isloggedin, FALSE) = FALSE;