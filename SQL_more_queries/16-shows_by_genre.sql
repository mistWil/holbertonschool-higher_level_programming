-- Script: 16-shows_by_genre.sql

-- Select all shows and their genres
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;