DROP TABLE IF EXISTS actors;
CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
 );

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08-10-1970', 5),
('George','Clooney','06-05-1961', 2),
('Gal', 'Gadot', '05-05-1985', '1'),
('Natalie', 'Portman', '05-05-1981', '2');

UPDATE actors SET first_name = 'Maty' WHERE first_name = 'Matt';

UPDATE actors SET number_oscars = 4 WHERE first_name = 'George' AND last_name = 'Clooney';

ALTER TABLE actors RENAME COLUMN age TO birthday;

SELECT * FROM actors;

