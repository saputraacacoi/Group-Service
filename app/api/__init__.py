from flask_restplus import Api

api = Api(version='1.0', title='group service', description='simple group service code')
ns  = api.namespace('v0.1', 'g service')