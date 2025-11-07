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
