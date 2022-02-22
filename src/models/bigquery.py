from src import api
from src.models.response import ResponseModel
from src.utils.namespace_creator import create_namespace

status = api.model("status", ResponseModel().get_model())

ns = create_namespace("chats", "Default status operations")

api.add_namespace(ns)
