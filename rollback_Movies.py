import pymysql
from db_connect import *

def rollback_Movies():

    is_success = True

    # reset auto-increment
    insert_stmt = "ALTER TABLE Games AUTO_INCREMENT = 1;"
    try:

        connection = create_connection()
        cursor = connection.cursor()

        insert_status = run_insert(cursor, insert_stmt)
        if insert_status is False:
            is_success = False
            return is_success

        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False

    except pymysql.Error as e:
        print "rollback_Games error: " + e.strerror

    return is_success