from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version = '1.0', title = 'Python Backend Template',
          description = 'A simple python backend API', doc = '/api/docs')
