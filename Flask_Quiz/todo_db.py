from tinydb import TinyDB, Query
from flask import current_app, g


def get_db():
    if 'todo_db' not in g:
        g.todo_db = TinyDB(current_app.config['TODODATABASE'],
                           default_table="posts")
        if g.todo_db.all() == []:
            g.todo_db.insert({'title': 'Make todo list app',
                          'body': 'powered by Python and Flask',
                          'author': 'Ian',
                          'date': '5:44pm 7/5/2018'})
    return g.todo_db

