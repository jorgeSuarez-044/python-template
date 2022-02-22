from flask_restx import Api

from src.models.person import ns as people_namespace
from src.models.status import ns as status_namespace

api = Api(version = '1.0', title = 'Python Backend Template',
          description = 'A simple python backend API', doc = '/api/docs')

api.add_namespace(people_namespace)
api.add_namespace(status_namespace)
