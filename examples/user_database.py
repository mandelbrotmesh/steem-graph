import sys
sys.path.append('../steem_graph')
from steem_graph import database as db
from steem import Steem


# In this example I assume I used the sqlite3 command line to
# create an empty database called steemit-local.db

database_name = "steemit-local.db"

# CREATE THE USER TABLE
db.setup_user_database(database_name)

# CREATE A USER
db.create_user("marnee", database_name)

# GET A COUNT OF THE USERS IN THE DATABASE
(COUNT,) = db.get_user_count(database_name)
print("Number of users in database is %i" % COUNT)

# PRINT A LIST OF THE FIRST 100 USERS
print("The first 100 users is: ")
for user in db.get_user_list(1, 100, database_name):
    print(user)

# GET THE LIST OF STEEMIT USERS
# AND ADD THEM TO THE DATABASE

STEEMIT = Steem()
ALL_USERS_LIST = STEEMIT.get_all_usernames()
for user in ALL_USERS_LIST:
    db.create_user(user, database_name)

# # # PRINT A LIST OF THE FIRST 100 USERS
print("The first 100 users is: ")
for user in db.get_user_list(1, 100, database_name):
    print(user)
