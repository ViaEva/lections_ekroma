from peewee import *
from settings import settings

db = PostgresqlDatabase(settings.db)


class Deputat(Model):
    name = CharField(max_length=100)
    phone = CharField(max_length=20, null = True)
    email = CharField(max_length=100, null = True)
    fraction = CharField(max_length=100)

    class Meta:
        database = db
