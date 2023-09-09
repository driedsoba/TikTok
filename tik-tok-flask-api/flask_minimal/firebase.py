import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../tik-tok-flask-api/credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
