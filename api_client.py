import time
import json
import tweepy
from db_connect import *

API_KEY = 'TExqX9uooP4WKwwEO7zwYnndm'
API_SECRET = '1ttEhO6IDMsg2kWc3bPwF9NBvNlQNcrvmtAAj5yqKXuBSktq2e'
TOKEN_KEY = '806222569938550786-4nHCZbYhgh5lgW80fu0Z2VddxDUFlca'
TOKEN_SECRET = 'Bx7klKQPjxLSZgeLwU1PyhEMMjCvrxo4ML5EyqK0rDZXx'

def get_api_instance():
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
  api_inst = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
  return api_inst

def do_data_pull(api_inst):

  sql_query = "select movie_id, title from Movies order by title"

  try: 
    conn = create_connection()
    db_cursor = conn.cursor()
    query_status = run_insert(db_cursor, sql_query)
    resultset = db_cursor.fetchall()

    for record in resultset:
      movie_id = record[0]
      title = record[1]

      rotten_query = "(#RottenTomatoes OR @RottenTomatoes OR url:rottentomatoes.com) AND "
      twitter_query = rotten_query + "'" + title + "'"
      print "twitter_query: " + twitter_query
      twitter_cursor = tweepy.Cursor(api_inst.search, q=twitter_query, lang="en").items(20)

      for tweet in twitter_cursor:
          json_str = json.dumps(tweet._json)
          print "found a " + title + " tweet"
          insert_stmt = "insert into Tweet(tweet_doc, movie_id) values(%s, %s)"
          run_prepared_stmt(db_cursor, insert_stmt, (json_str, movie_id))
          do_commit(conn)
  
  except pymysql.Error as e:
    print "pymysql error: " + e.strerror
  
  except tweepy.TweepError as twe:
    print "got a TweepError: " + twe.message
    if twe.message.endswith("429"):
      print "got rate limit error, sleeping for 15 minutes"
      time.sleep(60*15)
      print "finished sleeping. re-trying do_data_pull"
      do_data_pull(api_inst)

api_inst = get_api_instance()
do_data_pull(api_inst)