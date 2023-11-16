-- Script to list all genres by their rating sum

SELECT g.name, SUM(r.rate) as rating
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_show_ratings r ON sg.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
