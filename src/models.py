from peewee import Model, CharField, DateTimeField
from config import DB

class ChatGPTUser(Model):
    userToken = CharField()
    expireTime = DateTimeField()

    class Meta:
        database = DB
        table_name = 'chatgpt_user'
