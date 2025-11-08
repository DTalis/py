---Ex1 Task1
SET search_path TO movies, public;

SELECT 
    g.genre_name,
    m.title AS movie_title,
    m.popularity,
    RANK() OVER (
        PARTITION BY g.genre_name 
        ORDER BY m.popularity DESC
    ) AS rank_by_popularity
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g         ON mg.genre_id = g.genre_id;

---Ex1 Task2
SELECT
    pc.company_name,           
    m.title AS movie_title,
    m.revenue,
    NTILE(4) OVER (
        PARTITION BY pc.company_name
        ORDER BY m.revenue DESC
    ) AS revenue_quartile
FROM movie m
JOIN movie_company mc      ON m.movie_id = mc.movie_id     
JOIN production_company pc ON mc.company_id = pc.company_id; 

WITH ranked AS (
    SELECT
        pc.company_name,
        m.title AS movie_title,
        m.revenue,
        RANK() OVER (
            PARTITION BY pc.company_name
            ORDER BY m.revenue DESC
        ) AS rnk
    FROM movie m
    JOIN movie_company mc      ON m.movie_id = mc.movie_id
    JOIN production_company pc ON mc.company_id = pc.company_id
)
SELECT *
FROM ranked
WHERE rnk <= 3
ORDER BY company_name, rnk, revenue DESC;

---Ex1 Task3
SELECT
    g.genre_name,
    m.title        AS movie_title,
    m.budget,
    SUM(m.budget) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.title
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    )              AS running_total_budget
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g         ON mg.genre_id = g.genre_id
ORDER BY g.genre_name, m.title;

---Ex1 Task4
WITH most_recent AS (
    SELECT
        g.genre_name,
        FIRST_VALUE(m.title)       OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_title,
        MAX(m.release_date)        OVER (PARTITION BY g.genre_name)                               AS latest_release_date,
        ROW_NUMBER()               OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS rn
    FROM movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g         ON mg.genre_id = g.genre_id
)
SELECT genre_name, most_recent_title AS movie_title, latest_release_date AS release_date
FROM most_recent
WHERE rn = 1
ORDER BY genre_name;

WITH ranked AS (
    SELECT
        g.genre_name,
        m.title        AS movie_title,
        m.release_date,
        ROW_NUMBER() OVER (
            PARTITION BY g.genre_name
            ORDER BY m.release_date DESC
        ) AS rn
    FROM movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g         ON mg.genre_id = g.genre_id
)
SELECT genre_name, movie_title, release_date
FROM ranked
WHERE rn = 1
ORDER BY genre_name;

---Ex2 Task1
WITH actor_counts AS (
  SELECT 
      p.person_id,
      p.person_name,
      COUNT(DISTINCT mc.movie_id) AS movie_count
  FROM movie_cast mc
  JOIN person p ON p.person_id = mc.person_id
  GROUP BY p.person_id, p.person_name
)
SELECT
    person_name AS actor_name,
    movie_count,
    DENSE_RANK() OVER (ORDER BY movie_count DESC) AS dense_rank_by_appearances
FROM actor_counts
ORDER BY dense_rank_by_appearances, actor_name;

---Ex2 Task2
WITH director_avg AS (
  SELECT
      p.person_id,
      p.person_name AS director_name,
      AVG(m.vote_average) AS avg_rating
  FROM movie_crew cr
  JOIN person p  ON p.person_id = cr.person_id
  JOIN movie  m  ON m.movie_id   = cr.movie_id
  WHERE cr.job = 'Director'  -- при необходимости добавь: AND cr.department = 'Directing'
    AND m.vote_average IS NOT NULL
  GROUP BY p.person_id, p.person_name
),
ranked AS (
  SELECT
      director_name,
      avg_rating,
      RANK() OVER (ORDER BY avg_rating DESC) AS rnk
  FROM director_avg
)
SELECT director_name, avg_rating
FROM ranked
WHERE rnk = 1
ORDER BY director_name;

---Ex2 Task 3
WITH actor_movies AS (
  SELECT
      p.person_id,
      p.person_name AS actor_name,
      m.movie_id,
      m.title,
      m.release_date,
      COALESCE(m.revenue, 0) AS revenue
  FROM movie_cast mc
  JOIN person p ON p.person_id = mc.person_id
  JOIN movie  m ON m.movie_id   = mc.movie_id
)
SELECT
    actor_name,
    title AS movie_title,
    release_date,
    revenue,
    SUM(revenue) OVER (
        PARTITION BY actor_name
        ORDER BY release_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue_by_actor
FROM actor_movies
ORDER BY actor_name, release_date NULLS LAST, movie_title;

---Ex2 Task 4
WITH director_budget AS (
  SELECT
      p.person_id,
      p.person_name AS director_name,
      SUM(COALESCE(m.budget, 0)) AS total_budget
  FROM movie_crew cr
  JOIN person p ON p.person_id = cr.person_id
  JOIN movie  m ON m.movie_id   = cr.movie_id
  WHERE cr.job = 'Director'   -- при необходимости: AND cr.department = 'Directing'
  GROUP BY p.person_id, p.person_name
),
ranked AS (
  SELECT
      director_name,
      total_budget,
      ROW_NUMBER() OVER (ORDER BY total_budget DESC) AS rn
  FROM director_budget
)
SELECT director_name, total_budget
FROM ranked
WHERE rn = 1;