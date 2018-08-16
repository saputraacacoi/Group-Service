from app.api import api, ns
from flask_restplus import Resource


@ns.route('/group')
class GroupAPI(Resource):
    
    def post(self):
        """Creates a new Group."""
        create_group(request.json)
        return None, 201
    
    def get(self):
        """Returns list of Group."""
        return get_all_groups()
        



