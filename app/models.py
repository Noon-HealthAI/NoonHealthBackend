from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class SurveyResponseDB(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(String, nullable=False)
    responses = Column(Text, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    password_hash = Column(String, nullable=False)

    organization = Column(String, nullable=False)

    role = Column(String, default="user")