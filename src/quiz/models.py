from src.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime


class Quiz(Base):
    __tablename__ = "quiz"
    id: int = Column(Integer, nullable=False, index=True, primary_key=True)
    text_question: str = Column(String)
    text_answer: str = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())

    def __repr__(self):
        return self.text_question






