USE sakila;

-- 1a Display first and last name of all actors
SELECT first_name, last_name
FROM actor;

-- 1b Display actor full name in one column
SELECT concat_ws(" ", first_name, last_name) AS "Actor Name"
FROM actor;

-- 2a Return ID number, first name, and last name of actors with first name Joe
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name LIKE "joe";

-- 2b Display all actors whose last name contain 'GEN'
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE "%GEN%";

-- 2c Dispaly all actors whose last name contains 'LI', ordered by last name then first name
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE "%LI%"
ORDER BY last_name, first_name;

-- 2d Display country ID and country for Afghanistan, Bangladesh, and China
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a Create description column in actor table with data type Blob
ALTER TABLE actor
ADD COLUMN description BLOB;

-- 3b Drop description column from actor table
ALTER TABLE actor
DROP COLUMN description;

-- 4a Create a table of actor last names by count
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name;

-- 4b Filter to include only last names with at least two actors
SELECT last_name, COUNT(*) as name_count
FROM actor
GROUP BY last_name
HAVING name_count > 1;

-- 4c Change Groucho Williams to Harpo Williams
SET SQL_SAFE_UPDATES = 0;

UPDATE actor
	SET first_name = "Harpo"
    WHERE (first_name = "Groucho") AND (last_name = "Williams");

-- 4d Change all Harpos to Grouchos
UPDATE actor
	SET first_name = "Groucho"
    WHERE first_name = "Harpo";

-- 5a Query to locate schema of address table    
SHOW CREATE TABLE address;

-- 6a Join staff and address and display name with address
SELECT staff.first_name, staff.last_name, address.address
FROM staff JOIN address ON staff.address_id = address.address_id;

-- 6b Join staff and payment, display total amount sold by staff member
SELECT * FROM payment;

SELECT staff.first_name, staff.last_name, sum(payment_table.amount)
FROM staff JOIN 
	(SELECT * FROM payment WHERE payment_date >= '2005-08-01' AND payment.payment_date < '2005-09-01') as payment_table
    ON staff.staff_id = payment_table.staff_id
GROUP BY staff.staff_id;

-- 6c List each film and the number of actors listed for the film
SELECT * FROM film;
SELECT * FROM film_actor;

SELECT film.title as 'Movie', film_actor_count.actor_count as 'Number of Actors'
FROM film JOIN 
	(SELECT film_actor.film_id, COUNT(film_actor.actor_id) AS actor_count
	FROM film_actor
	GROUP BY film_actor.film_id) AS film_actor_count
ON film.film_id = film_actor_count.film_id;

-- 6d Find number of copis of 'Hunchback Impossible' in inventory
SELECT * FROM inventory;

SELECT t1.title AS 'Movie Name', COUNT(t1.inventory_id) as 'Number of Copies'
FROM
	(SELECT film.title, inventory.inventory_id
	FROM inventory JOIN film ON inventory.film_id = film.film_id
    HAVING film.title = 'Hunchback Impossible') AS t1;
    
-- 6e List the total paid by each customer
SELECT * FROM customer;
SELECT * FROM payment;

SELECT t1.customer_id AS 'ID', t1.first_name AS 'First Name', t1. last_name AS 'Last Name', SUM(amount) as 'Total Paid'
FROM
	(SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount
	FROM customer JOIN payment ON customer.customer_id = payment.customer_id) AS t1
GROUP BY t1.customer_id
ORDER BY t1.last_name;

-- 7a Display all english language movies that start with K and Q
SELECT * FROM film;
SELECT * FROM language;

SELECT * FROM
	(SELECT film.title AS title
	FROM film JOIN language ON film.language_id = language.language_id
	WHERE language.name = 'English') AS t1
WHERE t1.title LIKE 'K%' OR t1.title LIKE 'Q%';

-- 7b Display all actors who appear in 'Alone Trip'
SELECT * FROM film_actor;
SELECT * FROM actor;

SELECT first_name AS 'First Name', last_name AS 'Last Name'
FROM actor JOIN
	(SELECT actor_id 
    FROM film_actor JOIN film 
		ON film_actor.film_id = film.film_id
	WHERE film.title = 'Alone Trip') AS t1
    ON t1.actor_id = actor.actor_id;
    
-- 7c Return all Canadian customer email addresses
SELECT * FROM customer;
SELECT * FROM address;
SELECT * FROM city;
SELECT * FROM country;

SELECT email AS 'Customer Email'
FROM customer
JOIN
	(SELECT address_id
	FROM address
	JOIN
		(SELECT city_id FROM city JOIN
			(SELECT country_id
			FROM country
			WHERE country = 'Canada') AS t1
		ON city.country_id = t1.country_id) as t2
	ON address.city_id = t2.city_id) as t3
ON customer.address_id = t3.address_id;

-- 7d Return list of all movies categorized as family films
SELECT * FROM film_category;
SELECT * FROM category;

SELECT title
FROM film
JOIN
	(SELECT film_id
	FROM film_category
	JOIN
		(SELECT category_id
		FROM category
		WHERE name = 'Family') AS t1
	ON film_category.category_id = t1.category_id) AS t2
ON film.film_id = t2.film_id;

-- 7e Display most frequently rented movies in descending order
SELECT * FROM rental;
SELECT * FROM inventory;

SELECT film.title, t2.rentals
FROM film
JOIN
	(SELECT inventory.film_id, SUM(t1.rentals) AS rentals
	FROM inventory
	JOIN
		(SELECT inventory_id, COUNT(rental_id) AS rentals
		FROM rental
		GROUP BY inventory_id) AS t1
	ON inventory.inventory_id = t1.inventory_id
	GROUP BY film_id) AS t2
ON film.film_id = t2.film_id
ORDER BY rentals DESC;

-- 7f Calculate how many dollars each business brought in
SELECT * FROM store;
SELECT * FROM payment;
SELECT * FROM staff;

SELECT staff.store_id AS 'Store ID', t1.sales AS 'Store Revenue'
FROM staff
JOIN
	(SELECT staff_id, SUM(amount) AS sales
	FROM payment
	GROUP BY staff_id) AS t1
ON staff.staff_id = t1.staff_id;

-- 7g Display each store's ID, city, and Country
SELECT * FROM store;
SELECT * FROM address;
SELECT * FROM city;
SELECT * FROM country;

SELECT store_id AS 'Store ID', city AS 'City', country AS 'Country'
FROM country
JOIN
	(SELECT store_id, city, country_id
	FROM city
	JOIN
		(SELECT t1.store_id, t1.address_id, city_id
		FROM address
		JOIN
			(SELECT store_id, address_id
			FROM store) AS t1
		ON address.address_id = t1.address_id) AS t2
	ON city.city_id = t2.city_id) AS t3
ON country.country_id = t3.country_id;

-- 7h List the top five genres in gross revenue in descending order
SELECT * FROM payment;
SELECT * FROM rental;
SELECT * FROM inventory;
SELECT * FROM film_category;
SELECT * FROM category;

SELECT *
FROM
	(SELECT name AS 'Genre', revenue AS 'Revenue'
	FROM category
	JOIN
		(SELECT category_id, SUM(revenue) AS revenue
		FROM film_category
		JOIN
			(SELECT film_id, SUM(revenue) AS revenue
			FROM inventory
			JOIN
				(SELECT inventory_id, revenue
				FROM rental
				JOIN
					(SELECT rental_id, SUM(amount) AS revenue
					FROM payment
					GROUP BY rental_id) AS t1
				ON rental.rental_id = t1.rental_id) AS t2
			ON inventory.inventory_id = t2.inventory_id
			GROUP BY film_id) AS t3
		ON film_category.film_id = t3.film_id
		GROUP BY category_id) AS t4
	ON category.category_id = t4.category_id
	ORDER BY Revenue DESC) AS t5
LIMIT 5;

-- 8a Create a view to display the top 5 genres by revenue
CREATE VIEW Top_Five
AS (SELECT *
FROM
	(SELECT name AS 'Genre', revenue AS 'Revenue'
	FROM category
	JOIN
		(SELECT category_id, SUM(revenue) AS revenue
		FROM film_category
		JOIN
			(SELECT film_id, SUM(revenue) AS revenue
			FROM inventory
			JOIN
				(SELECT inventory_id, revenue
				FROM rental
				JOIN
					(SELECT rental_id, SUM(amount) AS revenue
					FROM payment
					GROUP BY rental_id) AS t1
				ON rental.rental_id = t1.rental_id) AS t2
			ON inventory.inventory_id = t2.inventory_id
			GROUP BY film_id) AS t3
		ON film_category.film_id = t3.film_id
		GROUP BY category_id) AS t4
	ON category.category_id = t4.category_id
	ORDER BY Revenue DESC) AS t5
LIMIT 5);

-- 8b Display top 5 genre view
SELECT * FROM sakila.top_five;

-- 8c Delete top 5 genre view
DROP VIEW top_five;