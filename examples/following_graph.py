from steem import Steem
from py2neo import Graph, Node, Relationship
import json
import time
import sys
sys.path.append('../steem_graph')
from steem_graph import graph as gdb
from steem_graph import database as db

database_name = "steemit-local.db"

# build my following graph
gdb.build_following_graph("marnee")

# get totall number of users
user_count = db.get_user_count(database_name)
print("User count is %i" % user_count)

user_list = db.get_user_list(1, 100000, database_name)
for id, username in user_list:
    print("creating %s: " % username)
    gdb.build_following_graph(username)
