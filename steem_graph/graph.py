from steem import Steem
from py2neo import Graph, Node, Relationship
import json
import time
import sys

info = Steem()
graph = Graph(user="neo4j", password="test")

def build_following_graph (follower):
    got_info = False
    following = []
    while not got_info:
        try:
            following = info.get_following(follower, 0, "blog", 100)
            got_info = True
        except: # in case get_following fails. sometimes it times out or you cant connect for some reason
            time.sleep(1)
            got_info = False
