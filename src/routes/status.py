from flask import Blueprint
from flask_restx import Resource

from src.models.status import status, ns
from src.utils.responses_handler import ResponsesHandler

blueprint = Blueprint('status', __name__)


@ns.route('/')
class Status(Resource):
    """Default api response to check availability"""

    @ns.doc('get_status')
    @ns.marshal_with(status)
    def get(self):
        """Get API status"""
        return ResponsesHandler.success()
