from flask_restx import fields

from src import api
from src.models.response import ResponseModel
from src.utils.namespace_creator import create_namespace

person = api.model("person", {
    'id': fields.String(description = 'Person id'),
    'name': fields.String(required = True, description = 'Person name'),
    'email': fields.String(required = True, description = 'Person email'),
    'age': fields.Integer(required = True, description = 'Person age'),
})

nested_person = fields.Nested(person, description = "People list")

def_response_model = ResponseModel()

person_response = api.model("person response",
                            def_response_model.add_data_field(nested_person))

people_response = api.model("people response",
                            def_response_model.add_data_field(fields.List(nested_person)))

ns = create_namespace('people', 'People sample operations')
api.add_namespace(ns)
