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