import pymysql
from db_connect import *

def rollback_Reviews():

    is_success = True


    # reset auto-increment
    insert_stmt = "ALTER TABLE Reviews AUTO_INCREMENT = 1;"
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
        print "rollback_Reviews error: " + e.strerror

    return is_success