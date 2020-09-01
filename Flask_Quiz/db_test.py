from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    body = Column(String)
    date = Column(String)
    author = Column(String)
    title = Column(String)

    def __repr__(self):
        return "<Posts(body='%s',date='%s',author='%s'," "title='%s'>" % (
            self.body,
            self.date,
            self.author,
            self.title,
        )


print "adding new db connection"
engine = create_engine("sqlite:///:test", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db = Session()

print "marker ho"
if db.query(Post).first() is None:
    print "it is nothing"

db.add(
    Post(
        title="fixing the initial db seeding",
        body="What he said",
        date="8-2-2018",
        author="Ian Clark",
    )
)

if db.query(Post).first():
    print "something here"
