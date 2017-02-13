use Database427;
drop table if exists Tweet;
create table Tweet (
  tweet_id varchar(32) generated always
     as (json_unquote(json_extract(tweet_doc, '$.id_str'))) stored primary key,
  screen_name varchar(32) generated always
     as (json_unquote(json_extract(tweet_doc, '$.user.screen_name'))) stored,
  created_at datetime generated always
     as (str_to_date(json_unquote(json_extract(tweet_doc, '$.created_at')),
     '%a %b %d %H:%i:%s +0000 %Y')) stored,
  tweet_doc json,
  movie_id int,
  foreign key (movie_id) references Movie(movie_id)
);  