USE world;
SELECT * FROM languages
WHERE languages.language = 'Slovene';

SELECT countries.name AS 'Country', languages.language AS 'Language', languages.percentage AS '% of population fluent'
FROM languages
LEFT JOIN countries
ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY	percentage DESC;

USE world;
SELECT language, percentage
FROM languages
WHERE language = 'Slovene'
GROUP BY language ASC, percentage DESC;
-----
SELECT COUNT(cities.id) AS 'number of cities in: ', countries.name AS 'Country Name'
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;
-------------
SELECT cities.population AS 'Number of Residents', cities.name AS 'City'
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000;
-----------------
SELECT countries.name AS 'Country Name', languages.language AS 'Language Spoken',languages.percentage AS 'Percent Lang. Spoken'
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 88
ORDER BY languages.percentage DESC;
---------------
SELECT countries.name AS 'Country Name', countries.surface_area AS 'Surface Area', countries.population AS 'Population'
FROM countries
WHERE countries.surface_area < 500 AND countries.population > 100000;
----------------

SELECT countries.name AS 'Country',countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 65;
----------------
SELECT countries.name AS 'Argentina', cities.name AS 'City', cities.district AS 'District',cities.population AS 'Population'
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;
-----------------
SELECT countries.region AS 'Country Region', COUNT(countries.name) AS 'Number of Countries'
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.name) DESC;



