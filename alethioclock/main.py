import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from config import SERVICE_ACCOUNT_PATH
from config import SERVICE_ADDRESS


cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://alethioclock.firebaseio.com/'
})

ref = db.reference(SERVICE_ADDRESS)

print(ref.get())