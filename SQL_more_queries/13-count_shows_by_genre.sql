-- lising number os shows with same genre
SELECT genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre
HAVING COUNT(tv_shows.id) > 0
ORDER BY number_of_shows DESC
