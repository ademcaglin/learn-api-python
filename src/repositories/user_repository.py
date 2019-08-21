from tinydb import TinyDB, Query
db = TinyDB('db.json')


def get_user(name):
    return db.table('users').search(Query().name.search(name))


def insert_user(name, age):
    db.table("users").insert({'name': name, 'age': age})
    return
