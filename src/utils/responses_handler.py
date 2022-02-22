"""Util function to build responses to be used in API endpoints"""


class ResponsesHandler:
    """Simple util class with functions to create successful or error responses easily"""

    @staticmethod
    def success(data = None):
        """Function to generate a successful response"""
        return {'success': True, 'data': data}

    @staticmethod
    def error(api, error_code = 500, error_message = 'Unexpected error', data = None):
        """Function to generate an error response"""
        return api.abort(error_code, error_message, data = data, success = False)
