import sqlalchemy
from flask import current_app, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Post(Base):
    __tablename__ = 'post'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    body = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.String)
    author = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return "<Posts(body='%s',date='%s',author='%s'," \
               "title='%s'>" % (self.body, self.date, self.author,
                                self.title)


def get_db():
    if 'todo_db' not in g:
        g.engine = sqlalchemy.create_engine('sqlite:///instance/:memory',
                                            echo=True)
        Base.metadata.create_all(g.engine)
        g.Session = sessionmaker(bind=g.engine)
        g.todo_db = g.Session()
        g.todo_db.add(Post(body='hi',date='today',author='me',title='no'))
    return g.todo_db
