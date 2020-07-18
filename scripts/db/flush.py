import os

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

# This script flushes the local db so that we do not need to restart docker-compose to do it.
# Useful in testing/development scenarios and when continuously modifying model objects that will be written to the db.

def flush(g):
    g.V().drop().iterate()

def main():
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    print('Flushing existing vertices in local db...')
    flush(g)
    print('Done.')

    remote.close()

if __name__ == '__main__':
    main()