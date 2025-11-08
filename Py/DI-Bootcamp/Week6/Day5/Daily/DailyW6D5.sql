SET search_path TO movies, public;

---Task 1 — Average Budget Growth Rate per Production Company
WITH company_budgets AS (
    SELECT 
        pc.company_name,
        m.title,
        m.release_date,
        m.budget,
        LAG(m.budget) OVER (
            PARTITION BY pc.company_name 
            ORDER BY m.release_date
        ) AS prev_budget
    FROM movie m
    JOIN movie_company mc      ON m.movie_id   = mc.movie_id     
    JOIN production_company pc ON mc.company_id = pc.company_id  
    WHERE m.budget IS NOT NULL AND m.budget > 0
),
growth_rates AS (
    SELECT
        company_name,
        (budget - prev_budget) * 1.0 / prev_budget AS growth_rate
    FROM company_budgets
    WHERE prev_budget IS NOT NULL AND prev_budget > 0
)
SELECT 
    company_name,
    ROUND(AVG(growth_rate) * 100, 2) AS avg_budget_growth_percent
FROM growth_rates
GROUP BY company_name
ORDER BY avg_budget_growth_percent DESC NULLS LAST;

---Task 2 — Most Consistently High-Rated Actor
WITH avg_rating AS (
    SELECT AVG(vote_average) AS overall_avg_rating
    FROM movie
    WHERE vote_average IS NOT NULL
),
actor_high_rated AS (
    SELECT 
        p.person_name AS actor_name,     
        COUNT(DISTINCT m.movie_id) AS high_rated_movies
    FROM movie_cast mc
    JOIN person p ON p.person_id = mc.person_id  
    JOIN movie  m ON m.movie_id   = mc.movie_id  
    CROSS JOIN avg_rating
    WHERE m.vote_average IS NOT NULL
      AND m.vote_average > avg_rating.overall_avg_rating
    GROUP BY p.person_name
),
ranked AS (
    SELECT 
        actor_name,
        high_rated_movies,
        RANK() OVER (ORDER BY high_rated_movies DESC) AS rnk
    FROM actor_high_rated
)
SELECT actor_name, high_rated_movies
FROM ranked
WHERE rnk = 1
ORDER BY actor_name;

---Task 3 — Rolling Average Revenue (last 3 movies) per Genre
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.release_date,
    m.revenue,
    ROUND(
        AVG(m.revenue) OVER (
            PARTITION BY g.genre_name 
            ORDER BY m.release_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2
    ) AS rolling_avg_revenue
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id         
JOIN genre g         ON mg.genre_id = g.genre_id          
WHERE m.revenue IS NOT NULL
ORDER BY g.genre_name, m.release_date;

---Task 4 — Highest-Grossing Movie Series (by shared keywords)
WITH keyword_revenue AS (
    SELECT 
        k.keyword_id,
        k.keyword_name,
        SUM(m.revenue) AS total_revenue
    FROM movie m
    JOIN movie_keywords mk ON m.movie_id  = mk.movie_id     -- or m.id
    JOIN keyword k         ON mk.keyword_id = k.keyword_id  -- from 02_keyword.sql
    WHERE m.revenue IS NOT NULL
    GROUP BY k.keyword_id, k.keyword_name
),
ranked AS (
    SELECT 
        keyword_name,
        total_revenue,
        RANK() OVER (ORDER BY total_revenue DESC) AS rnk
    FROM keyword_revenue
)
SELECT keyword_name AS series_name, total_revenue
FROM ranked
WHERE rnk = 1;