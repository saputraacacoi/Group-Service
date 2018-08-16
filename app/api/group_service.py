from flask import jsonify, request
from app.api import api, ns
from flask_restplus import Resource, fields
from app.models.groups import Group, GroupSchema, db

group_fields = api.model('Group', {
    'name': fields.String,
    'keterangan': fields.String
})

group_schema = GroupSchema(many=True)

@ns.route('/group')
class GroupListAPI(Resource):    

    def get(self):
        """Returns list of Group."""
        queryset = Group.query.all()
        queryset = Group_schema.dump(queryset).data
        return jsonify({

            'data': queryset,
            'message': 'data have been successfully fetched',
            'error': False
        })

    @api.doc(body=group_fields)
    def post(self):
        """Creates a new Group."""
        data = request.get_json(force=True)
        if data:
            group = Group()
            group.name = data['name']
            group.keterangan = data['keterangan']
            db.session.add(group)
            db.session.commit()
        return jsonify({
            'data' : [
                group.__serialize__()
            ],
            'message': 'data have been successfully saved',
            'error': False 
        })
@ns.route('/group/<int:id>')
class GroupAPI(Resource):
    def get(self, id):
        group = Group.query.get(id)
        if group:
            return jsonify({
                'data': [
                    group.__serialize__()
                ],
                'message': 'successfully!',
                'error': False
            })

        return jsonify({
            'data': [],
            'message': 'data not found',
            'error': False
        })

    @api.doc(body=group_fields)
    def put(self, id):
        data = request.get_json(force=True)
        group = User.query.get(id)
        group.name = data['name']
        group.keterangan = data['keterangan']
        db.session.add(group)
        db.session.commit()

        return jsonify({
            'data': [
                group.__serialize__()
            ],
            'message': 'successfully updated',
            'error': False
        })

    def delete(self, id):
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()

        return jsonify({
            'data': [
                group.__serialize__()
            ],
            'message': 'successfully deleted',
            'error': False
        })
