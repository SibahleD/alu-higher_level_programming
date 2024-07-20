-- listing values with certain conditions
SELECT score, name
FROM second_table
WHERE NOT name = ''
ORDER BY score DESC;
