from flask import Flask, Blueprint
from app.api import api
import os


basedir = os.path.dirname(os.path.abspath(__file__))
db_file = 'sqlite:///' + os.path.join(basedir, './db/group.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import models
from app.api.group_service import ns as group_api

blueprint = Blueprint('api', __name__, url_prefix='/service')
api.init_app(blueprint)

api.add_namespace(group_api)

app.register_blueprint(blueprint)