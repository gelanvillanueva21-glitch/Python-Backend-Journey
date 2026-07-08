from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///Data/users_info.db"


Base = declarative_base()

class Authentication(Base):
    __tablename__ = "Users"
    
    id = Column(
        Integer, 
        primary_key = True, 
        index = True)
    username = Column(
        String, 
        unique = True, 
        nullable = False)
    password = Column(
        String,
        nullable = False
    )



engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

