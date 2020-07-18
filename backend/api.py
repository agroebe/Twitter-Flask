from flask import Blueprint
from flask import jsonify

import os

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __

api_blueprint = Blueprint('api', __name__) # maybe just make this api then alias it.

@api_blueprint.route('/<username>/tweets')
def show_user(username):
    graph = Graph()
    remote = DriverRemoteConnection('ws://' + os.environ['DB_ENDPOINT'] + ':8182/gremlin', 'g')
    g = graph.traversal().withRemote(remote)

    user = g.V().hasLabel('user').has('username', username).valueMap(False).by(__.unfold())

    if not user.hasNext():
        content = { 'response': '404: User not found' }
        return content, 404

    properties = user.next()

    return jsonify(user=properties)

    

# @app.route('/' methods=['POST', 'GET'])
#     if request.method == 'POST':
#         print('post')
#     else:
#         print('get')

