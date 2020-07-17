import os
import names
import datetime

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

AMOUNT_TO_SEED = 10

def seed_users():
    for i in range(0, AMOUNT_TO_SEED):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        username = first_name + '_' + last_name

        g.addV('user').property('username', username).property('join_date', 'Today').next()

        print('Added user to local db:', username)

def main():
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    seed_users()

    remote.close()

if __name__ == '__main__':
    main()