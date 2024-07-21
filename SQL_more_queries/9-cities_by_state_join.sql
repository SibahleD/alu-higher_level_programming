-- Listing all cities by state
SELECT cities.id, cities.name
FROM cities, states
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
