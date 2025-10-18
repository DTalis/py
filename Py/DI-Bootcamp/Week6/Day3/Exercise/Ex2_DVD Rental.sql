--1) Use UPDATE to change the language of some films. Make sure that you use valid languages.
SELECT l.language_id, l.name
FROM language AS l;

UPDATE film AS f SET language_id = (
  SELECT l.language_id FROM language AS l WHERE l.name = 'Italian'
)
WHERE f.title IN ('ACADEMY DINOSAUR', 'ACE GOLDFINGER');

SELECT * FROM film;

--2) Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
SELECT customer_id FROM customer;
/* 	•	Foreign keys ensure data integrity: you cannot point to a store or address that doesn’t exist.
	•	RETURNING fetches the new address_id so you can use it immediately.
	•	Using valid FKs avoids insert or update on table ... violates foreign key constraint. */

--3) We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE IF EXISTS customer_review;
DROP TABLE IF EXISTS customer_review CASCADE;

--4) Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) FROM rental AS r
WHERE r.return_date IS NULL;

--5) Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.film_id, f.title, f.replacement_cost
FROM rental AS r
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film AS f ON f.film_id = i.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.film_id, f.title, f.description
FROM film        AS f
JOIN film_actor  AS fa ON fa.film_id = f.film_id
JOIN actor       AS a  ON a.actor_id = fa.actor_id
WHERE a.first_name = 'Penelope'
  AND a.last_name  = 'Monroe'
  AND f.description ILIKE '%sumo%';

--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT f.film_id, f.title, f.length, f.rating
FROM film           AS f
JOIN film_category  AS fc ON fc.film_id    = f.film_id
JOIN category       AS c  ON c.category_id = fc.category_id
WHERE c.name = 'Documentary'
  AND f.length < 60
  AND f.rating = 'R';

--The 3rd film : A film that his friend Matthew Mahan rented. 
--He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT DISTINCT f.film_id, f.title
FROM customer  AS cu
JOIN rental    AS r  ON r.customer_id  = cu.customer_id
JOIN payment   AS p  ON p.rental_id    = r.rental_id
JOIN inventory AS i  ON i.inventory_id = r.inventory_id
JOIN film      AS f  ON f.film_id      = i.film_id
WHERE cu.first_name = 'Matthew'
  AND cu.last_name  = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date >= DATE '2005-07-28'
  AND r.return_date <  DATE '2005-08-02';

--The 4th film : His friend Matthew Mahan watched this film, as well. 
--It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT DISTINCT f.film_id, f.title, f.replacement_cost
FROM customer  AS cu
JOIN rental    AS r  ON r.customer_id  = cu.customer_id
JOIN inventory AS i  ON i.inventory_id = r.inventory_id
JOIN film      AS f  ON f.film_id      = i.film_id
WHERE cu.first_name = 'Matthew'
  AND cu.last_name  = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;

  