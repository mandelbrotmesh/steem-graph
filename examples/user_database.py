import sys
sys.path.append('../steem_graph')

from steem_graph import database as db

(COUNT,) = db.get_user_count()
print("Number of users in database is %i" % COUNT)

for user in db.get_user_list(1,100):
    print(user)
