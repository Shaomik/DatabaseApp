import pymysql
import csv
from db_connect import *
#finished in 0.1s

def import_Movies():
	
	is_success = True
	insert_prefix = "insert into Movies (movie_id, title, genre) values (%s, %s, %s)"

	try:

		connection = create_connection()
		cursor = connection.cursor()

		csvfile = open("movies.csv", "rb")
		reader = csv.reader(csvfile)
		for i, row in enumerate(reader):
			if i == 0: continue
			for j, val in enumerate(row):
				if j == 1:
					title = val
				elif j == 2:
					genre = val


			movie_id = i 

			insert_status = run_prepared_stmt(cursor, insert_prefix, (movie_id,title,genre))
			if insert_status is False:
				is_success = False
				return is_success
		
		commit_status = do_commit(connection)
		if commit_status is False:
			is_success = False
			return is_success

	except pymysql.Error as e:
		print "import_Movies error: " + e.strerror

	return is_success

#is_success = import_Movies()
#print "is_success", is_success