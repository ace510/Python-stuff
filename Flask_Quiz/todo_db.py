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
    if 'db' not in g:
        print 'adding new db connection'
        g.engine = sqlalchemy.create_engine('sqlite:///instance/:memory',
                                            echo=True)
        Base.metadata.create_all(g.engine)
        g.Session = sessionmaker(bind=g.engine)
        g.db = g.Session()

        # this code adds sample data into the db if nothing is there
        if g.db.query(Post).first() is None:
            g.db.add(Post(body='I\'ve done it', date='8/2/2018',
                          author='Ian Clark',
                          title='Achieved minimum viable product'))
            g.db.add(Post(body='changed to relational database', date='today',
                          author='Ian Clark', title='next, to remove posts'))
    return g.db
