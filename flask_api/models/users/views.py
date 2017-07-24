from flask import Blueprints


user_blueprint = Blueprints('users', __name__)


@user_blueprint.route('/register', methods=['POST'])
def register():
    return ''

@user_blueprint.route('/login', methods=['POST'])
def login():
    return ''
