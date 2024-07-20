-- listing records with similar values
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
