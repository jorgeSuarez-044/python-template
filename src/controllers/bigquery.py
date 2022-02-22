import json
import os
from google.cloud import bigquery
from google.oauth2 import service_account
from src.utils.responses_handler import ResponsesHandler
from src import api

credentials = service_account.Credentials.from_service_account_file(
    os.environ["BIG_QUERY_KEY"],
    scopes = ["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(
    credentials = credentials,
    project = credentials.project_id,
)

QUERY = """SELECT clientEmail, clientId, clientName, conversationUpdateTime, COUNT(*) AS quantity
           FROM `bpsmart-dev-projects.Breadlovers.chats_messenger_conversations` GROUP BY clientEmail,
           clientId, clientName, conversationUpdateTime order by quantity desc"""

# noinspection PyBroadException
class BigQuery:
    """This class allows to get values from GCP bigquery through a query"""

    def get_all(self):
        """Returns all chats"""
        try:
            queryResult = []
            for row in client.query(QUERY):
                queryResult.append(row)
            return ResponsesHandler.success(json.dumps(str(queryResult)))
        except Exception:
            return ResponsesHandler.error(api, 500, "unable to connect to server")
