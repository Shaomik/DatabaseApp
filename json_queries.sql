
-- Shows the count of the tweets for  movie id
select movies.movie_id, 
count(*) tweet_count from Movies join Tweet 
on movies.movie_id = tweet.movie_id 
group by movies.movie_id;

-- Finds the count of the tweets by the movie genre
select movies.genre, count(*) as tweet_count 
from Movies 
join Tweet 
on movies.movie_id = tweet.movie_id 
group by movies.genre;

-- Shows the count of the tweets by the movie title and screen name of twitters
select movies.title, tweet.screen_name, count(*) as tweet_count 
from Movies join Tweet 
where movies.movie_id = tweet.movie_id 
group by tweet.screen_name;

-- number of tweets by movies with movie name
select movies.title, movies.movie_id, count(*) as tweet_count 
from Movies join Tweet  
on movies.movie_id = tweet.movie_id 
group by movies.title, movies.movie_id 
order by tweet_count desc;

-- number of tweets by movies without losing empty groups
select movies.title, movies.movie_id, count(tweet.tweet_id) as tweet_count 
from Movies left outer join Tweet 
on movies.movie_id = tweet.movie_id 
group by movies.title, movies.movie_id 
order by tweet_count desc;

