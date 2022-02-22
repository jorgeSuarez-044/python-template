from flask_restx import fields


class ResponseModel:
    """Default BPSmart endpoints model"""

    def __init__(self):
        self.model = {
            "success": fields.Boolean(required = True,
                                      description = "Whether the call was successful or not",
                                      default = False),
            "message": fields.String(required = False,
                                     description = "An error message if call errored"),
        }

    def add_data_field(self, data_field):
        """Creates a copy of the default model and adds the given field as 'data'"""
        new_model = self.model.copy()
        new_model['data'] = data_field
        return new_model

    def get_model(self):
        """Creates a copy of the default model and returns it"""
        return self.model.copy()
