import pymysql
from rollback_Games import *
from rollback_Publisher import *
from rollback_Reviews import *
from rollback_Movies import *
from import_Games import *
from import_Publisher import *
from import_Reviews import *
from import_Movies import *

# rollback Game table
is_success = rollback_Games()

if is_success is True:
    print "rollback_Games: successful"
else:
    print "rollback_Games: failed"

# rollback Publisher table
is_success = rollback_Publisher()

if is_success is True:
    print "rollback_Publisher: successful"
else:
    print "rollback_Publisher: failed"

# rollback Reviews table
is_success = rollback_Reviews()

if is_success is True:
    print "rollback_Reviews: successful"
else:
    print "rollback_Reviews: failed"

# rollback Movies table
is_success = rollback_Movies()

if is_success is True:
    print "rollback_Movies: successful"
else:
    print "rollback_Movies: failed"





# populate Game table
is_success = import_Games()

if is_success is True:
	print "import_Game: successful"
else:
	print "import_Game: failed"

# populate Publisher table
is_success = import_Publisher()

if is_success is True:
	print "import_Publisher: successful"
else:
	print "import_Publisher: failed"

# populate Reviews table
is_success = import_Reviews()

if is_success is True:
	print "import_Reviews: successful"
else:
	print "import_Reviews: failed"

# populate Movies table
is_success = import_Movies()

if is_success is True:
	print "import_Movies: successful"
else:
	print "import_Movies: failed"
