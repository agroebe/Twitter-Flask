from flask import Blueprint
from flask import jsonify

import os

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/users/')
def list_users():
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    print(g.V().hasLabel('user').valueMap(True).by(__.unfold()).next())

    return jsonify(user='hi'), 200

@api_blueprint.route('/api/users/<username>/')
def list_user(username):
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    user = g.V().hasLabel('user').has('username', username).valueMap(False).by(__.unfold())

    if not user.hasNext():
        content = { 'response': '404: User not found' }
        return content, 404

    properties = user.next()

    return jsonify(user=properties), 200

@api_blueprint.route('/api/tweets/<username>/')
def list_tweets(username):
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    user = g.V().hasLabel('user').has('username', username)

    if not user.hasNext():
        content = { 'response': '404: User not found' }
        return content, 404

    count = user.out('tweeted').count().next()
    print(count)

    return jsonify(user='hi'), 200