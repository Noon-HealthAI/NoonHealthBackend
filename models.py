from sqlalchemy import Column, Integer, String, Text
from database import Base


class SurveyResponseDB(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(String, nullable=False)
    responses = Column(Text, nullable=False)