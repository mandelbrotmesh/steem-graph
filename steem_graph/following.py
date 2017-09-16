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
            print ("Retrying ... .")
            time.sleep(1)
            got_info = False
    follower_node = Node("USER", name=follower)
    for followed in following:
        f1 = followed["following"]
        following_node = Node("USER", name=f1)
        rel = Relationship(follower_node, "FOLLOWING", following_node)
        graph.merge(rel)

def build_following_for_all_users:
    print ("Getting all user names")
    all_users = info.get_all_usernames()
    iteration = 0
    for user in all_users:
        print ("Iteration %i " % iteration)
        print ("Build following graph for %s " % user)
        if iteration <= 10000:  # here to keep it from running forever until I can figure out how to do this in batches or parallel
            print ("Getting user %s " % user)
            build_following_graph(user)
            iteration = iteration + 1

def build_following_for_user(username):
    print("Building following graph for user %s" % username)
    build_following_graph(username)