USE sakila;
SELECT * FROM film;
DESCRIBE film;

-- Count the film
SELECT COUNT(film_id) AS 'Total films'
FROM film;

SELECT rating, COUNT(film_id) AS 'Total films'
FROM film
GROUP BY rating;

SELECT  rental_duration, AVG(rental_rate) AS 'Average rental rate'
FROM film
GROUP BY rental_duration;

select * from customer;
SELECT * FROM payment;

SELECT AVG(rental_rate) AS 'Average cost to rent'
FROM film;

SELECT rating, AVG(rental_rate) AS 'Average cost to rent'
FROM film
GROUP BY rating;

SELECT SUM(replacement_cost)
FROM film;

SELECT rating, SUM(replacement_cost) AS 'Total replacement cost'
FROM film
GROUP BY rating;

SELECT Max(length) AS 'Longest', MIN(length) AS 'Shortest'
FROM film;

SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
HAVING customer_id < 5;



SELECT title, film_id
FROM film
WHERE title = 'Early Home';

SELECT *
FROM inventory
WHERE film_id = 268;

SELECT i.inventory_id, i.film_id, i.store_id
FROM inventory i
JOIN film f
ON (i.film_id = f.film_id)
WHERE f.title = 'Early Home';

SELECT *
FROM inventory
WHERE film_id
IN (
SELECT film_id
FROM film
WHERE title = 'Early Home'
);



SELECT * from address;

SELECT city_id, city
FROM city
WHERE city LIKE 'Q%';

SELECT district
FROM city c
JOIN address a
ON (c.city_id = a.city_id)
WHERE city LIKE 'Q%';

SELECT * FROM CUSTOMER;

SELECT first_name, last_name
FROM customer cus
WHERE address_id IN
(
  SELECT address_id
  FROM address a
  WHERE city_id IN
  (
    SELECT city_id
    FROM city 
    WHERE city LIKE 'Q%'
  ) 
);

-- Creating views
CREATE VIEW total_sales AS 
SELECT s.store_id, SUM(amount) AS Gross
FROM payment p
JOIN rental r
ON (p.rental_id = r.rental_id)
JOIN inventory I
ON (i.inventory_id = r.inventory_id)
JOIN store s
ON (s.store_id = i.store_id)
GROUP BY s.store_id;


SELECT * FROM inventory;
SELECT * FROM film;

SELECT inventory.film_id, title
FROM inventory
JOIN film
ON (inventory.film_id = film.film_id);


SELECT title, 
(SELECT COUNT(*) 
    FROM inventory 
    WHERE film.film_id = inventory.film_id ) AS 'Number of Copies'
    FROM film;
    
SELECT * FROM num_copies

SELECT * FROM film f
LEFT OUTER JOIN film_actor fa
ON (f.film_id = fa.film_id)
WHERE fa.film_id IS NULL;

SELECT * FROM rental;

SELECT first_name, last_name
FROM actor
WHERE actor_id
IN (
	SELECT actor_id
	FROM film_actor
	WHERE film_id
	IN (
		SELECT film_id
		FROM film
		WHERE title = "Alter Victory"
		)
	);
    
SELECT title
    FROM film
    WHERE film_id
    IN (
        SELECT film_id
            FROM inventory
            WHERE inventory_id
            IN (
                SELECT inventory_id
                    FROM rental
                    WHERE staff_id
                        IN (
                            SELECT staff_id
                                FROM staff
                                WHERE last_name = "Stephens" AND first_name = "Jon"
                            )
                )
        );
        
  
  
  CREATE TABLE animals_all ( id INTEGER(11) AUTO_INCREMENT
NOT NULL, animal_species VARCHAR(30) NOT NULL,
owner_name VARCHAR(30) NOT NULL, PRIMARY KEY (id) );

INSERT INTO animals_all (animal_species, owner_name)
VALUES ("Dog", "Bob");
INSERT INTO animals_all (animal_species, owner_name)
VALUES ("Fish", "Bob");
INSERT INTO animals_all (animal_species, owner_name)
VALUES ("Cat", "Kelly");
INSERT INTO animals_all (animal_species, owner_name)
VALUES ("Dolphin", "Aquaman");

CREATE TABLE animals_location (
id INTEGER(11) AUTO_INCREMENT NOT NULL,
location VARCHAR(30) NOT NULL,
animal_id INTEGER(10) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (animal_id) REFERENCES animals_all(id) );

INSERT INTO animals_location (location, animal_id)
VALUES ("Doghouse", 1);
INSERT INTO animals_location (location, animal_id)
VALUES ("Fish tank", 2);
INSERT INTO animals_location (location, animal_id)
VALUES ("Bed", 3);
INSERT INTO animals_location (location, animal_id)
VALUES ("Ocean", 4);


CREATE TABLE animals_all ( id INTEGER(11) AUTO_INCREMENT NOT
NULL, animal_species VARCHAR(30) NOT NULL, owner_name
VARCHAR(30) NOT NULL, PRIMARY KEY (id) );

CREATE TABLE animals_location (
id INTEGER(11) AUTO_INCREMENT NOT NULL,
location VARCHAR(30) NOT NULL,
animal_id INTEGER(10) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (animal_id) REFERENCES animals_all(id) );

select * from customer;

VALUES ("Ocean", 4);

CREATE TABLE customer_email (
	email_id INT auto_increment not null,
    email VARCHAR(30),
    customer_id SMALLINT(5),
    primary key(email_id),
    Foreign key (customer_id) REFERENCES customer(customer_id)
    );