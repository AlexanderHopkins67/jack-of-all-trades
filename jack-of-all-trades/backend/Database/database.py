from sqlalchemy import create_engine, CHAR, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    public_id = Column(String(60),unique=True, nullable=False, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    hashedPass = Column(String(60), unique=True, nullable=False)

    def __init__(self, public_id, username, hashedPass):
        self.public_id = public_id
        self.username = username
        self.hashedPass = hashedPass

    def __repr__(self):
        return f"{self.public_id}"

Engine = create_engine(url="sqlite:///jack-of-all-trades/backend/Database/database.db", echo=True)
Base.metadata.create_all(bind=Engine)
        
Session = sessionmaker(bind=Engine)
session = Session()
