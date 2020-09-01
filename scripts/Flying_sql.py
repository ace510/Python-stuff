import pyodbc
import sqlalchemy
import random
import string

# conn = pyodbc.connect('''DRIVER={ODBC Driver 17 for SQL Server};
#                       SERVER=orb514810;
#                       DATABASE=Pyton;
#                       UID=Python;PWD=python''')

rotary_engine = sqlalchemy.create_engine("mssql+pyodbc://Python:python@python_DSN")

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

all_ur_base = declarative_base()
Session = sessionmaker(bind=rotary_engine)
from sqlalchemy import Column, Integer, String
from sqlalchemy import UniqueConstraint


class User(all_ur_base):
    __tablename__ = "Pyton"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    favorite_number = Column(Integer)
    UniqueConstraint("name")

    def __repr__(self):
        return (
            "<User(name= %s, favorite number = %s >" % self.name,
            self.favorite_number,
        )


Session = Session()
for i in range(10000):
    number = random.randrange(1000)
    name = "".join(random.choice(string.ascii_letters) * 5)
    trial_user = User(name=name, favorite_number=number)
    Session.add(trial_user)
Session.commit()
