from peewee import *
from playhouse.sqlcipher_ext import SqlCipherDatabase

# Defer initialization of the database until the script is executed from the
# command-line.
db = SqlCipherDatabase()


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize(passphrase):
    db.init('diary.db', passphrase=passphrase, kdf_iter=64000)
    Entry.create_table()
