import os
import names
import datetime

from models.user import User
from models.tweet import Tweet

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

AMOUNT_TO_SEED = 10

def seed_users(g):
    for i in range(0, AMOUNT_TO_SEED):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        username = first_name + '_' + last_name

        user = User(
            username='andrew_groebe',
            password='andrew123',
            display_name='Andrew P. Groebe',
            join_date='August 2017',
            bio='Software Engineering Student and tech enthusiast'
        )

        user_vertex_id = user.write(g)

        tweet = Tweet(
            contents='This is my first tweet, so Hello World!'
        )

        tweet_vertex_id = tweet.write(g)

        g.V(user_vertex_id).addE('tweeted').to(g.V(tweet_vertex_id)).next()

def main():
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    seed_users(g)

    remote.close()

if __name__ == '__main__':
    main()