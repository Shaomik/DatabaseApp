# -*- coding: utf-8 -*-
import pymysql
from db_connect import *

sqlInject = [ "; drop table", "; truncate table", "; delete from", "or 1=1"]

def print_menu():
    print "1. Show review information of games with user review score and reviewers greater than user entered value "
    print "2. Show all review information of games on user selected platform"
    print "3. Show publisher info of games by Electronic Arts ordered by platform"
    print "4. Shows game information ordered by user entered column"
    print "5. Shows game information ordered by platform"
    print "6. Shows game information of user selected genre ordered by title"
    print "7. Shows game information of user selected movie"
    print "8. Shows publisher information ordered by platform"
    print "9. Shows release date of games where number of reviewers is greater than 55 and groups them by platform"
    print "10. Shows games titles grouped by platform where publisher id is greater than 25"
    print "11. Groups movies and games with the same genre and is ordered by genre of the game"
    print "12. Find distinct movies using left outer join with game_id being equal to movie_id"
    print "13. Show games review score and number of reviewers with game id being equal to the score id"
    print "14. Ceate view 1: shows title of the game with left outer join on game_id equals movie_id and also which are released after 2005"
    print "15. Show view 2: shows which genre are made which publisher name of the game with right outer join on game_id of Publisher equals game_id of Games and ordered it by genre of Games"
   

def query1(a,b):

    is_success = True
    query = "SELECT * FROM Reviews WHERE score >  'a' AND reviewers > 'b'"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "reviewers query failed: " + e.strerror

    return is_success
    
    
def query2(a):
    
    is_success = True
    query = "SELECT * FROM Reviews WHERE platform =" + "'" + a + "'"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "platform query failed: " + e.strerror

    return is_success

def query3():
    
    is_success = True

    query = "SELECT * FROM Publisher WHERE pubName = 'Electronic Arts, Inc.' Order BY platform"

    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "query3 failed: " + e.strerror

    return is_success    

def query4(a):
    
    is_success = True

    query = "SELECT * FROM Games ORDER BY " + "'" + a + "'"

    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "query4 failed: " + e.strerror

    return is_success

def query5():
    
    is_success = True

    query = "SELECT * FROM Games ORDER BY platform"

    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "query5 failed: " + e.strerror

    return is_success    

def query6(a):
    
    is_success = True

    query = "SELECT * FROM Games WHERE Games.genre =" + "'" + a + "'"

    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "query6 failed: " + e.strerror

    return is_success    
   
def query7(a):
    
    is_success = True
    query = "SELECT * FROM Movies WHERE title =" + "'" + a + "'"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "query7 failed: " + e.strerror

    return is_success    

def query8():

    is_success = True
    query = "SELECT * FROM Publisher ORDER BY platform"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "platform query failed: " + e.strerror

    return is_success

def query9():

    is_success = True
    query = "SELECT Games.release_date, COUNT(reviewers) FROM (Reviews INNER JOIN Games ON Games.game_id=Reviews.score_id) GROUP BY Games.platform HAVING COUNT(reviewers > 55)"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "reviewers query failed: " + e.strerror

    return is_success

def query10():

    is_success = True
    query = "SELECT Games.title, COUNT(Publisher.pub_id) FROM (Publisher INNER JOIN Games ON Games.game_id=Publisher.game_id) GROUP BY Games.platform HAVING COUNT(Publisher.pub_id > 25)"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "pb_id query failed: " + e.strerror

    return is_success

def query11():

    is_success = True
    query = "SELECT * FROM (Movies INNER JOIN Games ON Games.genre=Movies.genre) ORDER BY Games.genre"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "title query failed: " + e.strerror

    return is_success

def query12():

    is_success = True
    query = "SELECT DISTINCT Movies.title FROM (Movies LEFT OUTER JOIN Games ON Games.game_id=Movies.movie_id)"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "game_id query failed: " + e.strerror

    return is_success

def query13():

    is_success = True
    query = "SELECT Games.title, Reviews.score, Reviews.reviewers  FROM Games LEFT OUTER JOIN Reviews ON Games.game_id=Reviews.score_id"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "score query failed: " + e.strerror

    return is_success

def query14():

    is_success = True
    query = "CREATE VIEW view1 as SELECT Games.title FROM Movies LEFT OUTER JOIN Games ON Games.game_id=Movies.movie_id WHERE Games.release_date > 2005"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "score query failed: " + e.strerror

    return is_success

def query15():

    is_success = True
    query = "CREATE VIEW view2 as SELECT Publisher.pubName, Games.genre FROM (Publisher RIGHT OUTER JOIN Games ON Publisher.game_id=Games.game_id) ORDER BY Games.genre"
    try: 
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_insert(cursor, query)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""    
        for row in results:
            print row
        print "" 

    except pymysql.Error as e:
        is_success = False
        print "score query failed: " + e.strerror

    return is_success


    
while True:          
    print_menu()   
    choice = int(input("Enter your choice [1-15]: "))
     
    if choice== 1:     
        a = str(input("Enter score greater than desired:"))
        b = str(input("Enter reviewers greater than desired:"))
        print "You have chosen to show Choice 1. Here are the results:"
        while a in sqlInject:
            a = str(input("Invalid entry, try again: "))
        while b in sqlInject:
            b = str(input("Invalid entry, try again: "))
        query1(a,b)
    elif choice==2:
        a = raw_input("Enter platform: ")
        print "You have chosen to show Choice 2. Here are the results: "
        while a in sqlInject:
            a = raw_input("Invalid entry, try again: ")
        query2(a)
    elif choice==3:
        print "You have chosen to show Choice 3. Here are the results: "
        query3()    
    elif choice==4:
        a = raw_input("Enter column name in Game tables:")
        print "You have chosen to show Choice 4. Here are the results: "
        while a in sqlInject:
            a = raw_input("Invalid entry, try again: ")
        query4(a)
    elif choice==5:
        print "You have chosen to show Choice 5. Here are the results: "
        query5()
    elif choice==6:
        a = raw_input("Enter Genre :")
        print "You have chosen to show Choice 6. Here are the results: "
        while a in sqlInject:
            a = raw_input("Invalid entry, try again: ")
        query6(a)
    elif choice==7:
        a = raw_input("Enter Movie Title:")
        print "You have chosen to show Choice 7. Here are the results: "
        while a in sqlInject:
            a = raw_input("Invalid entry, try again: ")
        query7(a)
    elif choice==8:
        print "You have chosen to show Choice 8. Here are the results: "
        query8()           
    elif choice==9:
        print "You have chosen to show Choice 9. Here are the results: "
        query9()
    elif choice==10:
        print "You have chosen to show Choice 10. Here are the results: "
        query10()
    elif choice==11:
        print "You have chosen to show Choice 11. Here are the results: "
        query11()
    elif choice==12:
        print "You have chosen to show Choice 12. Here are the results: "
        query12()
    elif choice==13:
        print "You have chosen to show Choice 13. Here are the results: "
        query13()   
    elif choice==14:
        print "You have chosen to show Choice 14. Results are added to the database "
        query14() 
    elif choice==15:
        print "You have chosen to show Choice 15. Results are added to the database "
        query15()                              
    else:
        raw_input("Wrong choice! Try again: ")
         