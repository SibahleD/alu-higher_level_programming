-- Listing all cities by state
USE hbbtn_0d_usa
SELECT cities.id, cities.name, (states.name WHERE state.id = cities.id) AS state_name
FROM cities, states
ORDER BY cities.id ASC;
