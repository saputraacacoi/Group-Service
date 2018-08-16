from app.api import api, ns
from flask_restplus import Resource


@ns.route('/group')
class UserAPI(Resource):
    def get(self):
        return {
            'group': 'group service api'
        }

