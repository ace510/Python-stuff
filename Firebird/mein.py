import sqlalchemy
import fdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker

# print(sqlalchemy.__version__)

want_echo = False
#enable to do echo
engine = create_engine('firebird+fdb://SYSDBA:45952877@//home/ihclark/database/test.fdb', echo=want_echo)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class User1(Base):
    __tablename__ = 'users1'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)




# Column(Integer, Sequence('user_id_seq'), primary_key=True)


ed_user = User1(name='ed', fullname='Ed Jones', nickname='edsnickname')
# print(ed_user.nickname)
session.add(ed_user)

our_user = session.query(User1).filter_by(name='ed').first()

# print(repr(our_user))

# if ed_user is our_user:
#    print('true')

session.add_all([
    User1(name='Ian', fullname='Ian Clark', nickname='Ace'),
    User1(name='Violet', fullname='Violet Love', nickname='Little Ratto'),
    User1(name='Dan', fullname='Dan Man', nickname='The') ])

ed_user.nickname = 'eddie'

print(session.dirty)

session.commit()

print(ed_user.id)