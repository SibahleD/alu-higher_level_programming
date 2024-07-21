-- Listing all cities by state
SELECT cities.id, cities.name, (states.name WHERE state.id = cities.id) as state_name
FROM cities, states
ORDER BY cities.id ASC;
