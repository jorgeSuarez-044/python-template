from flask import Blueprint
from flask_restx import Resource

from src.controllers.people import PeopleDAO
from src.models.person import person, person_response, people_response, ns

blueprint = Blueprint('people', __name__)

DAO = PeopleDAO(ns)
DAO.create({'name': 'Jahir'})


@ns.route('/')
class PersonList(Resource):
    """Shows a list of all people, and lets you POST to add new persons"""

    @ns.doc('list_people')
    @ns.marshal_with(people_response)
    def get(self):
        """List all persons"""
        return DAO.get_all()

    @ns.doc('create_person')
    @ns.expect(person)
    @ns.marshal_with(person_response, code = 201)
    def post(self):
        """Create a new person"""
        return DAO.create(ns.payload), 201


@ns.route('/<int:person_id>')
@ns.response(404, 'Person not found')
@ns.param('id', 'The person identifier')
class Person(Resource):
    """Show a single person item and lets you delete them"""

    @ns.doc('get_person')
    @ns.marshal_with(person_response)
    def get(self, person_id):
        """Fetch a given resource"""
        return DAO.get(person_id)

    @ns.doc('delete_person')
    @ns.response(204, 'Person deleted')
    def delete(self, person_id):
        """Delete a person given its identifier"""
        DAO.delete(person_id)
        return '', 204

    @ns.expect(person)
    @ns.marshal_with(person_response)
    def put(self, person_id):
        """Update a person given its identifier"""
        return DAO.update(person_id, ns.payload)
