import pymysql
import csv
from db_connect import *

#finished in 0.3s

def import_Games():
	
	is_success = True
	insert_prefix = "insert into Games (game_id, title, release_date, platform, genre) values (%s,%s,%s,%s,%s)"

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
				elif j == 1:
					title = val
				elif j == 7:
					release_date = int(val)
				
				elif j == 17:
					genre = val


			game_id = i 

			insert_status = run_prepared_stmt(cursor, insert_prefix, (game_id,title,release_date,platform,genre))
			if insert_status is False:
				is_success = False
				return is_success
		
		commit_status = do_commit(connection)
		if commit_status is False:
			is_success = False
			return is_success

	except pymysql.Error as e:
		print "import_Games error: " + e.strerror

	return is_success

#is_success = import_Games()
#print "is_success", is_success

	