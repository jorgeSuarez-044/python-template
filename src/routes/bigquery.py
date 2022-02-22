from flask import Blueprint
from flask_restx import Resource
from src.controllers.bigquery import BigQuery
from src.models.bigquery import ns

blueprint = Blueprint('chats', __name__)

query = BigQuery()

@ns.route('/')
@ns.response(500, 'unable to connect to server')
class Chat(Resource):
    """Show all chats"""

    @ns.doc('get_chats')
    def get(self):
        """Fetch a given resource"""
        return query.get_all()
