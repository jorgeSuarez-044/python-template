import os

from firebase_admin import credentials, firestore, initialize_app

from src import api
from src.utils.responses_handler import ResponsesHandler

GCP_ENV = None
# noinspection PyBroadException
try:
    GCP_ENV = os.environ['GCP_ENV']
except Exception as e:
    GCP_ENV = 'dev'
    print(e)

PROJECT_ID = None
# noinspection PyBroadException
try:
    PROJECT_ID = os.environ[GCP_ENV + '_project_id']
except Exception as e:
    print(e)

if GCP_ENV is None or PROJECT_ID is None:
    raise Exception('GCP environment or GCP project id are not set properly')

print('Running {} on {}'.format(PROJECT_ID, GCP_ENV))

# Initialize Firestore DB
CRED = credentials.Certificate('./certificate.json') if GCP_ENV is None \
    else credentials.ApplicationDefault()
initialize_app(CRED, {'projectId': PROJECT_ID})
db = firestore.client()
people_collection = db.collection('people')


# noinspection PyBroadException
class PeopleDAO:
    """Data Access Object to handle people crud"""

    @staticmethod
    def doc_ref_to_dict(doc_ref):
        """
        Attempts to transform a firestore document into a dictionary, adding id as dictionary field
        """
        try:
            doc_data = doc_ref.to_dict()
            doc_data['id'] = doc_ref.id
            return doc_data
        except Exception:
            return None

    def get_all(self):
        """Returns the whole people list"""
        people = []
        try:
            for doc_ref in people_collection.stream():
                people.append(self.doc_ref_to_dict(doc_ref))
        except Exception:
            pass
        return ResponsesHandler.success(people)

    def get(self, person_id = None):
        """Try and get a single person given its id"""
        try:
            doc_ref = people_collection.document(person_id)
            return ResponsesHandler.success(self.doc_ref_to_dict(doc_ref))
        except Exception:
            return ResponsesHandler.error(api, 404, "Person {} doesn't exist".format(person_id), [])

    def create(self, data):
        """Add a new person to the list"""
        try:
            doc_ref = people_collection.document()
            doc_ref.set(data)
            return ResponsesHandler.success(self.doc_ref_to_dict(doc_ref))
        except Exception:
            return ResponsesHandler.error(api, 500, "Unable to save person data on Firestore")

    def update(self, person_id, data):
        """Update a person's data"""
        try:
            doc_ref = people_collection.document(person_id)
            doc_ref.update(data)
            return ResponsesHandler.success(self.doc_ref_to_dict(doc_ref))
        except Exception:
            return ResponsesHandler.error(api, 404, "Person {} doesn't exist".format(person_id), [])

    def delete(self, person_id):
        """Delete a person from the list"""
        try:
            doc_ref = people_collection.document(person_id)
            doc_ref.delete()
            return ResponsesHandler.success(self.doc_ref_to_dict(doc_ref))
        except Exception:
            return ResponsesHandler.error(api, 404, "Person {} doesn't exist".format(person_id), [])
