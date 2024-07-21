-- Listing all cities by state
SELECT cities.id, cities.name, (SELECT states.name WHERE state.id = cities.id) AS state_name
FROM cities, states
ORDER BY cities.id ASC;
