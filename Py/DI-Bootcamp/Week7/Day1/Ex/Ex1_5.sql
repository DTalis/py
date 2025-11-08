---Ex1
DROP TABLE IF EXISTS df_employee;

CREATE TEMP TABLE df_employee AS
SELECT
  CONCAT(s.employee_id, '_', TO_CHAR(to_timestamp(s."date", 'DD/MM/YYYY HH24:MI'), 'YYYYMMDD')) AS id,
  TO_CHAR(to_timestamp(s."date", 'DD/MM/YYYY HH24:MI'), 'YYYY-MM') AS month_year,
  s.employee_id,
  COALESCE(s.employee_name, e.employee_name_emp) AS employee_name,
  e."GEN(M_F)" AS gender,
  NULLIF(e.age, '')::INT AS age,
  NULLIF(REPLACE(s.salary, ',', '.'), '')::NUMERIC AS salary,
  f.function_group,
  c.company_name,
  c.company_city,
  c.company_state,
  c.company_type,
  c.const_site_category
FROM salaries s
LEFT JOIN employees e ON e.employee_code_emp = s.employee_id
LEFT JOIN functions f ON f.function_code = s.func_code
LEFT JOIN companies c ON c.company_name = s.comp_name;

SELECT COUNT(*) AS rows_in_df_employee FROM df_employee;
SELECT * FROM df_employee LIMIT 20;

---Ex2

SELECT * FROM df_employee LIMIT 50;


UPDATE df_employee
SET
  id                  = NULLIF(TRIM(id), ''),
  month_year          = NULLIF(TRIM(month_year), ''),
  employee_name       = NULLIF(TRIM(employee_name), ''),
  gender              = NULLIF(TRIM(gender), ''),
  function_group      = NULLIF(TRIM(function_group), ''),
  company_name        = NULLIF(TRIM(company_name), ''),
  company_city        = NULLIF(TRIM(company_city), ''),
  company_state       = NULLIF(TRIM(company_state), ''),
  company_type        = NULLIF(TRIM(company_type), ''),
  const_site_category = NULLIF(TRIM(const_site_category), '')

;


SELECT *
FROM df_employee
WHERE
      id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL       OR gender = ''
   OR age IS NULL
   OR salary IS NULL
   OR function_group IS NULL      OR function_group = ''
   OR company_name IS NULL        OR company_name = ''
   OR company_city IS NULL        OR company_city = ''
   OR company_state IS NULL       OR company_state = ''
   OR company_type IS NULL        OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = ''
;


DELETE FROM df_employee
WHERE
      id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL
   OR salary IS NULL
;

SELECT COUNT(*) AS rows_after_clean FROM df_employee;
SELECT * FROM df_employee LIMIT 20;

---Ex3
SELECT
  company_name,
  COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY company_name
ORDER BY employee_count DESC;

---Ex4
-- TOTAL EMPLOYEES BY CITY + PERCENTAGE OF TOTAL
WITH city_counts AS (
  SELECT
    COALESCE(company_city, 'Unknown') AS city,
    COUNT(DISTINCT employee_id)       AS employees
  FROM df_employee
  GROUP BY COALESCE(company_city, 'Unknown')
)
SELECT
  city,
  employees,
  ROUND(100.0 * employees / SUM(employees) OVER (), 2) AS pct_of_total
FROM city_counts
ORDER BY employees DESC;


--TOTAL NUMBER OF EMPLOYEES EACH MONTH
WITH monthly_counts AS (
  SELECT
    month_year,
    COUNT(DISTINCT employee_id) AS employees
  FROM df_employee
  GROUP BY month_year
)
SELECT *
FROM monthly_counts
ORDER BY month_year;


--AVERAGE NUMBER OF EMPLOYEES PER MONTH (OVER ALL MONTHS)
WITH monthly_counts AS (
  SELECT
    month_year,
    COUNT(DISTINCT employee_id) AS employees
  FROM df_employee
  GROUP BY month_year
)
SELECT
  ROUND(AVG(employees)::numeric, 2) AS avg_employees_per_month
FROM monthly_counts;


--EXERCISE 5
--MINIMUM AND MAXIMUM NUMBER OF EMPLOYEES THROUGHOUT ALL MONTHS
WITH monthly AS (
  SELECT
    month_year,
    COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY month_year
)
SELECT
  'Minimum employees' AS metric,
  MIN(employee_count) AS value,
  STRING_AGG(month_year, ', ') FILTER (WHERE employee_count = (SELECT MIN(employee_count) FROM monthly)) AS months_with_min
FROM monthly
UNION ALL
SELECT
  'Maximum employees' AS metric,
  MAX(employee_count) AS value,
  STRING_AGG(month_year, ', ') FILTER (WHERE employee_count = (SELECT MAX(employee_count) FROM monthly)) AS months_with_max
FROM monthly;


--MONTHLY AVERAGE NUMBER OF EMPLOYEES BY FUNCTION GROUP
WITH monthly_function AS (
  SELECT
    month_year,
    function_group,
    COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY month_year, function_group
)
SELECT
  function_group,
  ROUND(AVG(employee_count)::numeric, 2) AS avg_employees_per_month
FROM monthly_function
GROUP BY function_group
ORDER BY avg_employees_per_month DESC;


--ANNUAL AVERAGE SALARY
WITH salary_data AS (
  SELECT
    TO_CHAR(date_trunc('year', TO_DATE(month_year || '-01', 'YYYY-MM-DD')), 'YYYY') AS year,
    AVG(salary) AS avg_salary
  FROM df_employee
  WHERE salary IS NOT NULL
  GROUP BY TO_CHAR(date_trunc('year', TO_DATE(month_year || '-01', 'YYYY-MM-DD')), 'YYYY')
)
SELECT
  year,
  ROUND(avg_salary, 2) AS avg_annual_salary
FROM salary_data
ORDER BY year;