import sqlalchemy
import fdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
import pyodbc

# print(sqlalchemy.__version__)
with open('.token', r) as file:
    engine_string = file.readline()
    

want_echo = False
# enable to do echo
engine = create_engine(engine_string, echo=want_echo)
sql_engine = create_engine('mssql+pyodbc://squirrel')



# create the engine, in this case Freebired
Base = declarative_base()
Base.metadata.create_all(engine)
# declarative mapping as opposed to a classical
Session = sessionmaker(bind=engine)
session = Session()
# creates a new session, all CRUD is done against the session

class User1(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String())
    fullname = Column(String())
    nickname = Column(String())

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
    # Chance here, is not needed, just looks pretty




# Column(Integer, Sequence('user_id_seq'), primary_key=True)


ed_user = User1(name='ed', fullname='Ed Jones', nickname='edsnickname')
# do this to create a new element of User1, attached to variable ed_user
# print(ed_user.nickname)
session.add(ed_user)
# add the new element to the session

session.commit()
our_user = session.query(User1).filter_by(name='ed').first()

# print(repr(our_user))

# if ed_user is our_user:
#    print('true')

session.add_all([
    User1(name='Ian', fullname='Ian Clark', nickname='Ace'),
    User1(name='Violet', fullname='Violet Love', nickname='Little Ratto'),
    User1(name='Dan', fullname='Dan Man', nickname='The') ])

print(session.dirty)

session.commit()
