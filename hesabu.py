from peewee import *
from os import path
db_connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(db_connection, "hesabu.db"))


class Hesabu(Model):
    principle = IntegerField()
    rate = IntegerField()
    time = IntegerField()

    interest = principle * rate * time

    pi = IntegerField()
    radius = IntegerField()
    height = IntegerField()

    volume = pi * radius * height

    class Meta:
        database = db


Hesabu.create_table(fail_silently=True)