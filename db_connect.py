import pymysql


def create_connection():
	try:
		connection = pymysql.connect(host="",   # MySQL hostname
                                     user="",        # MySQL username, default is root
                                     passwd="",   # MySQL password
                                     db="")        # MySQL db name	
	except pymysql.Error as error:
		print "connection error: ", error

	return connection


def run_insert(cursor, insert_stmt):	
	is_success = True
	try:
		cursor.execute(insert_stmt)	    
	except pymysql.Error as error:
		print "insert error: ", error
		is_success = False
	return is_success

def run_prepared_stmt(cursor, stmt, paramtrs):
	is_success = True
	try:
		cursor.execute(stmt, paramtrs)
	except pymysql.Error as error:
		print "Error: ", error
		is_success = False
	return is_success

def do_commit(connection):
	is_success = True
	try:
		connection.commit()  
	except pymysql.Error as error:
		print "commit error: ", error
		is_success = False
	return is_success

def destroy_connection(connection):
	connection.close()
