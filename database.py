from mongoengine import *

from config import DATABASE_NAME, DATABASE_LOGIN, DATABASE_PASSWORD

connect(DATABASE_NAME, username=DATABASE_LOGIN, password=DATABASE_PASSWORD)

LANGUAGES = ['ru']
ADMINS = ['226261608']


class User(Document):
    user_id = IntField(required=True)
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    state = StringField()
    language = StringField(choices=LANGUAGES, default=LANGUAGES[0])


class BitmexAccount(Document):
    api_key = StringField(required=True)
    name = StringField(required=True)
    is_main = BooleanField(default=False)
