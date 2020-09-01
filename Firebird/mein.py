import sqlalchemy
import fdb
import random
import string
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker

# import pyodbc
# no ODBC for you, come back next year

# print(sqlalchemy.__version__)
with open(".token", "r") as file:
    engine_string = file.readline()

want_echo = False
# enable to do echo
engine = create_engine(engine_string, echo=want_echo)
# sql_engine = create_engine('mssql+pyodbc://squirrel')
# again, MSSQL bad


# create the engine, in this case Freebired
Base = declarative_base()
Base.metadata.create_all(engine)
# declarative mapping as opposed to a classical
Session = sessionmaker(bind=engine)
session = Session()
# creates a new session, all CRUD is done against the session


class User1(Base):
    __tablename__ = "users1"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String())
    fullname = Column(String())
    nickname = Column(String())

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )

    # Chance here, is not needed, just looks pretty


def delete_peep(session, num=0):
    for _ in range(num):
        person = session.query(User1).first()
        # print(repr(person))
        session.delete(person)
    session.commit()


def random_string(length):
    letters = string.ascii_letters
    output = ""
    for _ in range(length):
        output += random.choice(letters)

    return output


def add_peep(session, name, fullname, nickname):
    person = User1(name=name, fullname=name, nickname=name)
    # print(repr(person))
    session.add(person)
    session.commit()


def show_peep(session):
    person = session.query(User1).first()
    print(repr(person))


def main():

    add_peep(session, "Ian", "Ian Clark", "Ace")
    add_peep(session, "Dan", "Dan wallace", "Dan T Man")
    add_peep(session, "James", "James White", "Skipper")

    for _ in range(3):
        show_peep(session)
        delete_peep(session)


if __name__ == "__main__":
    main()
