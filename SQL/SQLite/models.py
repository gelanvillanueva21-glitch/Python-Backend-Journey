from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///SQL/SQLite/learning.db")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(bind = engine)
SessionLocal = sessionmaker(bind = engine)

database = SessionLocal()

# new_user = User(id = 1,
#                 username = "Gelan",
#                 password = "pizza123")

# database.add(new_user)
# database.commit()

user = database.query(User).filter(User.username == "Gelan").first()
print(user.id, user.username, user.password)
database.close()