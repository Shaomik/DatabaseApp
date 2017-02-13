import pymysql
import csv
from db_connect import *
#finished in 0.1s

def import_Reviews():

	is_success = True
	insert_prefix = "insert into Reviews (score_id, reviewers, game_id, platform, score) values (%s, %s, %s, %s, %s)"
	
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
				elif j == 22:
					score = int(val)
				elif j == 23:
					reviewers = int(val)
			game_id = i
			score_id = i

	
			insert_status = run_prepared_stmt(cursor, insert_prefix, (score_id,reviewers,game_id, platform, score))
			if insert_status is False:
				is_success = False
				return is_success
		
		commit_status = do_commit(connection)
		if commit_status is False:
			is_success = False
			return is_success

	except pymysql.Error as e:
		print "import_Reviewa error: " + e.strerror

	return is_success

#is_success = import_Reviews()
#print "is_success", is_success 