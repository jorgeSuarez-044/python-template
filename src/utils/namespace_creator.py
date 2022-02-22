from flask_restx import Namespace


def create_namespace(name: str, description: str = ''):
    """
    Creates a Namespace given the name and description, adding 'api/' as prefix to the namespace
    name
    """
    return Namespace('api/' + name, description = description)
