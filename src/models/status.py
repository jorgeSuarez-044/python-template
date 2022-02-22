from src.models.response import ResponseModel
from src.utils.namespace_creator import create_namespace

ns = create_namespace('status', 'Default status operations')

status = ns.model("status", ResponseModel().get_model())
