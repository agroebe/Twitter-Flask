from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/<username>')
def show_user(username):
    return username

# @app.route('/' methods=['POST', 'GET'])
#     if request.method == 'POST':
#         print('post')
#     else:
#         print('get')

