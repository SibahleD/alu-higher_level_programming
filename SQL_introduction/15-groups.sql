-- listing records with similar values
SELECT score, COUNT(score) AS number
GROUP BY score
HAVING COUNT(score) > 1;
