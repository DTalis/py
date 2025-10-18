--Get a list of all the languages, from the language table.
SELECT language_id, name FROM language;

--Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT f.title, f.description, l.name AS language_name
FROM film AS f
JOIN language AS l ON f.language_id = l.language_id;

--Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT l.name, f.title, f.description
FROM language AS l
LEFT JOIN film AS f ON f.language_id = l.language_id;

--Create a new table called new_film with the following columns : id, name. Add some new films to the table.
DROP TABLE IF EXISTS new_film CASCADE;
CREATE TABLE new_film (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);
INSERT INTO new_film (name) VALUES 
  ('Parallel Horizons'),
  ('Silent Harbor'),
  ('Crimson Lullaby');
SELECT * FROM new_film;

/* Create a new table called customer_review, which will contain film reviews that customers will make.
Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
It should have the following columns:
review_id – a primary key, non null, auto-increment.
film_id – references the new_film table. The film that is being reviewed.
language_id – references the language table. What language the review is in.
title – the title of the review.
score – the rating of the review (1-10).
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated.

Add 2 movie reviews. Make sure you link them to valid objects in the other tables. */
DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review (
  review_id SERIAL PRIMARY KEY,
  film_id INTEGER NOT NULL,
  language_id SMALLINT NOT NULL,
  title TEXT NOT NULL,
  score INTEGER CHECK (score BETWEEN 1 AND 10),
  review_text TEXT,
  last_update TIMESTAMPTZ DEFAULT NOW(),
  FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
  FOREIGN KEY (language_id) REFERENCES language(language_id)
);
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
(1, 1, 'Great movie!', 9, 'I really liked the story and visuals.'),
(2, 1, 'Not bad', 7, 'Interesting idea but too long.');
SELECT * FROM customer_review;

--Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 2;
SELECT * FROM customer_review;