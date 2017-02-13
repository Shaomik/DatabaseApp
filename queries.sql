SELECT *
FROM Reviews
WHERE score > ["80"] AND reviewers > ["5000"];

SELECT *
FROM Reviews
WHERE platform = ["Sony PSP"];

SELECT *
FROM Publisher
WHERE pubName = "Electronic Arts, Inc.";

SELECT * 
FROM Games
ORDER BY ["genre"];


SELECT * 
FROM Games
ORDER BY platform;

SELECT * 
FROM Games
WHERE genre = ["Action"]
ORDER BY title;

SELECT * 
FROM Movies
WHERE title = ["Sabrina (1995)"];

SELECT * 
FROM Publisher
ORDER BY platform;      


SELECT Games.release_date, COUNT(reviewers) 
FROM (Reviews
INNER JOIN Games ON Games.game_id=Reviews.score_id) 
GROUP BY platform
HAVING COUNT(reviewers > 55);
 
SELECT Games.title, COUNT(Publisher.pub_id) 
FROM (Publisher
INNER JOIN Games ON Games.game_id=Publisher.game_id) 
GROUP BY platform
HAVING COUNT(Publisher.pub_id > 25);


SELECT *
FROM (Movies
INNER JOIN Games ON Games.title=Movies.title) 
ORDER BY Games.genre;


SELECT DISTINCT title 
FROM (Movies
LEFT OUTER JOIN Games
ON Games.game_id=Movies.movie_id);

SELECT Reviews.score, Reviews.reviewers 
FROM Games
LEFT OUTER JOIN Reviews
ON Games.game_id=Reviewers.score_id;


CREATE VIEW view2 as
SELECT DISTINCT title 
FROM Movies
LEFT OUTER JOIN Games
ON Games.game_id=Movies.movie_id
WHERE Games.release_date > 2005;


CREATE VIEW view1 as
SELECT Publisher.pubName
FROM (Reviews
RIGHT OUTER JOIN Publisher ON Publisher.game_id=Reviews.game_id) 
ORDER BY Reviews.score;