---Task 1
SELECT
  m.medal_name,
  AVG(
    (SELECT gc.age
     FROM olympics.games_competitor gc
     WHERE gc.id = x.competitor_id)
  ) AS avg_age
FROM (
  SELECT DISTINCT ce.competitor_id, ce.medal_id
  FROM olympics.competitor_event ce
  WHERE ce.medal_id IN (1,2,3)
) x
JOIN olympics.medal m ON m.id = x.medal_id
GROUP BY m.medal_name
ORDER BY m.medal_name;

---Task 2
SELECT
  nr.region_name AS region,
  COUNT(DISTINCT pr.person_id) AS unique_competitors
FROM olympics.noc_region       nr
JOIN olympics.person_region    pr ON pr.region_id = nr.id
WHERE pr.person_id IN (
  SELECT gc.person_id
  FROM olympics.games_competitor gc
  WHERE gc.id IN (
    SELECT ce.competitor_id
    FROM olympics.competitor_event ce
    GROUP BY ce.competitor_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
  )
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;

---Task 3
DROP TABLE IF EXISTS tmp_competitor_medals;

CREATE TEMP TABLE tmp_competitor_medals AS
SELECT mc.competitor_id, mc.medal_count
FROM (
  SELECT
      ce.competitor_id,
      COUNT(*) AS medal_count
  FROM olympics.competitor_event ce
  WHERE ce.medal_id IN (1,2,3)
  GROUP BY ce.competitor_id
) AS mc;

SELECT *
FROM tmp_competitor_medals
WHERE medal_count > 2
ORDER BY medal_count DESC, competitor_id;

---Task 4
DELETE FROM tmp_competitor_medals t
WHERE NOT EXISTS (
  SELECT 1
  FROM olympics.competitor_event ce
  WHERE ce.competitor_id = t.competitor_id
    AND ce.medal_id IN (1,2,3)
);

---Task 1
UPDATE olympics.person p
SET height = (
  SELECT AVG(p2.height)
  FROM olympics.person p2
  JOIN olympics.person_region pr2 ON pr2.person_id = p2.id
  WHERE pr2.region_id = (
    SELECT pr.region_id
    FROM olympics.person_region pr
    WHERE pr.person_id = p.id
    LIMIT 1
  )
  AND p2.height IS NOT NULL
)
WHERE p.height IS NULL
  AND EXISTS (
    SELECT 1 FROM olympics.person_region prx
    WHERE prx.person_id = p.id
  );

 ---Task2 
DROP TABLE IF EXISTS tmp_multi_event_competitor;

CREATE TEMP TABLE tmp_multi_event_competitor AS
SELECT
    ce.competitor_id,
    gc.games_id,
    COUNT(DISTINCT ce.event_id) AS total_events
FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc
    ON gc.id = ce.competitor_id
GROUP BY ce.competitor_id, gc.games_id
HAVING COUNT(DISTINCT ce.event_id) > 1
ORDER BY total_events DESC;

SELECT *
FROM tmp_multi_event_competitor
ORDER BY total_events DESC, competitor_id, games_id;

---Task3
WITH medals_per_competitor AS (
  SELECT
      gc.id AS competitor_id,
      COALESCE(SUM(CASE WHEN ce.medal_id IN (1,2,3) THEN 1 ELSE 0 END), 0) AS medal_count
  FROM olympics.games_competitor gc
  LEFT JOIN olympics.competitor_event ce
    ON ce.competitor_id = gc.id
  GROUP BY gc.id
),

person_region_one AS (
  SELECT DISTINCT ON (pr.person_id)
         pr.person_id,
         pr.region_id
  FROM olympics.person_region pr
  ORDER BY pr.person_id, pr.region_id   
),


overall AS (
  SELECT AVG(medal_count::numeric) AS overall_avg
  FROM medals_per_competitor
)

SELECT
    nr.region_name,
    AVG(mpc.medal_count::numeric) AS avg_medals_per_competitor
FROM medals_per_competitor mpc
JOIN olympics.games_competitor gc
  ON gc.id = mpc.competitor_id
JOIN person_region_one pro
  ON pro.person_id = gc.person_id
JOIN olympics.noc_region nr
  ON nr.id = pro.region_id
GROUP BY nr.region_name
HAVING AVG(mpc.medal_count::numeric) > (SELECT overall_avg FROM overall)
ORDER BY avg_medals_per_competitor DESC, nr.region_name;

---Task4
-- Drop the temp table if it already exists
DROP TABLE IF EXISTS tmp_season_participation;

-- Create a temp table with participation counts per season
CREATE TEMP TABLE tmp_season_participation AS
SELECT
  gc.person_id,
  COUNT(*) FILTER (WHERE UPPER(g.season) = 'SUMMER') AS summer_participations,  -- Number of Summer participations
  COUNT(*) FILTER (WHERE UPPER(g.season) = 'WINTER') AS winter_participations,  -- Number of Winter participations
  BOOL_OR(UPPER(g.season) = 'SUMMER') AS has_summer,
  BOOL_OR(UPPER(g.season) = 'WINTER') AS has_winter
FROM olympics.games_competitor gc
JOIN olympics.games g
  ON g.id = gc.games_id
GROUP BY gc.person_id;

-- Show only athletes who took part in both Summer and Winter Games
SELECT person_id, summer_participations, winter_participations
FROM tmp_season_participation
WHERE has_summer AND has_winter
ORDER BY person_id;
