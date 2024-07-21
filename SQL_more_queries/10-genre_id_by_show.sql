-- Listing specific records
SELECT tv_shows.title, tv_shows.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows_id = tv_show_genres.show_id
ORdER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
