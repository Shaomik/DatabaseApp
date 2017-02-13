drop database if exists Database427;
create database Database427;
use Database427;

CREATE TABLE Games (
             game_id integer not null AUTO_INCREMENT primary key,
	         title varchar(100) not null, 
	         release_date integer not null,
             platform varchar(50) not null,
             genre varchar (100) not null
);
     
CREATE TABLE Reviews (
	         score_id integer primary key, 
	         reviewers integer,
	         game_id integer,
             platform varchar(50) not null,
             score integer not null,
             foreign key (game_id) references Games(game_id),
             foreign key (platform) references Games(platform)
);            
       
CREATE TABLE Publisher (
	         pub_id integer AUTO_INCREMENT primary key,
	         pubName varchar(300), 
	         platform varchar(100),
	         game_id integer,
	         foreign key (game_id) references Games(game_id),
	         foreign key (platform) references Games(platform)
);
       
CREATE TABLE Movies (
             movie_id integer not null AUTO_INCREMENT primary key,
             title varchar(500),
	         genre varchar(500)
   
);
       