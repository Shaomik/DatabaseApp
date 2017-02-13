import pymysql
import csv
from db_connect import *

#finished in 0.1s

def import_Publisher():
	
	is_success = True
	insert_prefix = "insert into Publisher (pub_id,pubName,platform, game_id) values (%s,%s,%s, %s)"

	try:

		connection = create_connection()
		cursor = connection.cursor()

		csvfile = open("Game.csv", "rb")
		reader = csv.reader(csvfile)
		for i, row in enumerate(reader):
			if i == 0: continue
			for j, val in enumerate(row):
				if j == 0:
					platform = val

				elif j == 16:
					pubName = val
			game_id = i
			pub_id = i

	
			insert_status = run_prepared_stmt(cursor, insert_prefix, (pub_id,pubName,platform,game_id))
			if insert_status is False:
				is_success = False
				return is_success
		
		commit_status = do_commit(connection)
		if commit_status is False:
			is_success = False
			return is_success

	except pymysql.Error as e:
		print "import_Publisher error: " + e.strerror

	return is_success

#is_success = import_Publisher()
#print "is_success", is_success