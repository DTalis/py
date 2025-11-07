/* =========================================================
   One-shot cleanup (safe to re-run)
   ========================================================= */
DROP TABLE IF EXISTS
  tmp_ex1_biseason_medalists,
  tmp_ex1_per_sport,
  tmp_ex1_agg,
  tmp_ex1_two_sport_medalists,
  tmp_ex2_per_comp_event,
  tmp_ex2_max_event_per_comp,
  tmp_ex2_region_totals,
  tmp_ex2_games_count,
  tmp_ex2_medaled_persons,
  tmp_ex2_participants_no_medals;


/* =========================================================
   🌟 EXERCISE 1: Detailed Medal Analysis
   ========================================================= */

-- ---------- Task 1 ----------
-- Competitors with ≥1 real medal in BOTH Summer and Winter (store + display)
CREATE TEMP TABLE tmp_ex1_biseason_medalists AS
SELECT
  gc.person_id,
  p.full_name,
  SUM(CASE WHEN g.season = 'Summer' AND md.medal_name IN ('Gold','Silver','Bronze') THEN 1 ELSE 0 END) AS summer_medals,
  SUM(CASE WHEN g.season = 'Winter' AND md.medal_name IN ('Gold','Silver','Bronze') THEN 1 ELSE 0 END) AS winter_medals,
  COUNT(*) FILTER (WHERE md.medal_name IN ('Gold','Silver','Bronze')) AS total_medals
FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON gc.id = ce.competitor_id
JOIN olympics.games g              ON g.id  = gc.games_id
JOIN olympics.person p             ON p.id  = gc.person_id
JOIN olympics.medal md             ON md.id = ce.medal_id
GROUP BY gc.person_id, p.full_name
HAVING SUM(CASE WHEN g.season = 'Summer' AND md.medal_name IN ('Gold','Silver','Bronze') THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN g.season = 'Winter' AND md.medal_name IN ('Gold','Silver','Bronze') THEN 1 ELSE 0 END) > 0;

-- Display Task 1
SELECT *
FROM tmp_ex1_biseason_medalists
ORDER BY total_medals DESC, full_name;


-- ---------- Task 2 ----------
-- Competitors who won medals in EXACTLY two different sports; show Top-3 by total medals

-- Step 1: per-competitor per-sport REAL medal counts
CREATE TEMP TABLE tmp_ex1_per_sport AS
SELECT
  gc.person_id,
  p.full_name,
  e.sport_id,
  COUNT(*) FILTER (WHERE md.medal_name IN ('Gold','Silver','Bronze')) AS medals_in_sport
FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON gc.id = ce.competitor_id
JOIN olympics.event e              ON e.id = ce.event_id
JOIN olympics.person p             ON p.id = gc.person_id
JOIN olympics.medal md             ON md.id = ce.medal_id
GROUP BY gc.person_id, p.full_name, e.sport_id;

-- Step 2: aggregate per competitor
CREATE TEMP TABLE tmp_ex1_agg AS
SELECT
  person_id,
  full_name,
  COUNT(DISTINCT sport_id) AS distinct_sports,
  SUM(medals_in_sport)     AS total_medals
FROM tmp_ex1_per_sport
GROUP BY person_id, full_name;

-- Step 3: keep exactly-two-sport medalists
CREATE TEMP TABLE tmp_ex1_two_sport_medalists AS
SELECT person_id, full_name, total_medals
FROM tmp_ex1_agg
WHERE distinct_sports = 2;

-- Display Task 2 (Top 3)
SELECT *
FROM tmp_ex1_two_sport_medalists
ORDER BY total_medals DESC, full_name
LIMIT 3;


/* =========================================================
   🌟 EXERCISE 2: Region And Competitor Performance
   ========================================================= */

-- ---------- Task 1 ----------
-- Top 5 regions by “max medals in a single event per competitor”
-- 1) medals per competitor per event (REAL medals)
CREATE TEMP TABLE tmp_ex2_per_comp_event AS
SELECT
  gc.person_id,
  ce.event_id,
  COUNT(*) FILTER (WHERE md.medal_name IN ('Gold','Silver','Bronze')) AS medals_in_event
FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON gc.id = ce.competitor_id
JOIN olympics.medal md             ON md.id = ce.medal_id
GROUP BY gc.person_id, ce.event_id;

-- 2) each competitor’s maximum medals in any single event
CREATE TEMP TABLE tmp_ex2_max_event_per_comp AS
SELECT
  person_id,
  MAX(medals_in_event) AS max_medals_one_event
FROM tmp_ex2_per_comp_event
GROUP BY person_id;

-- 3) map to regions and sum those maxima per region
CREATE TEMP TABLE tmp_ex2_region_totals AS
SELECT
  nr.region_name,
  SUM(m.max_medals_one_event) AS total_max_medals
FROM tmp_ex2_max_event_per_comp m
JOIN olympics.person_region pr ON pr.person_id = m.person_id
JOIN olympics.noc_region   nr ON nr.id = pr.region_id
GROUP BY nr.region_name;

-- Display Task 1 (Top 5)
SELECT region_name, total_max_medals
FROM tmp_ex2_region_totals
ORDER BY total_max_medals DESC, region_name
LIMIT 5;


-- ---------- Task 2 ----------
-- Competitors with >3 Games and NO real medals
-- 1) distinct Games per competitor
CREATE TEMP TABLE tmp_ex2_games_count AS
SELECT
  gc.person_id,
  p.full_name,
  COUNT(DISTINCT gc.games_id) AS games_played
FROM olympics.games_competitor gc
JOIN olympics.person p ON p.id = gc.person_id
GROUP BY gc.person_id, p.full_name;

-- 2) persons who have ANY real medal (exclude 'NA')
CREATE TEMP TABLE tmp_ex2_medaled_persons AS
SELECT DISTINCT gc.person_id
FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON gc.id = ce.competitor_id
JOIN olympics.medal md             ON md.id = ce.medal_id
WHERE md.medal_name IN ('Gold','Silver','Bronze');

-- 3) >3 games and no medals
CREATE TEMP TABLE tmp_ex2_participants_no_medals AS
SELECT
  g.person_id,
  g.full_name,
  g.games_played
FROM tmp_ex2_games_count g
LEFT JOIN tmp_ex2_medaled_persons m ON m.person_id = g.person_id
WHERE g.games_played > 3
  AND m.person_id IS NULL;

-- Display Task 2
SELECT *
FROM tmp_ex2_participants_no_medals
ORDER BY games_played DESC, full_name;