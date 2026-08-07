from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.sql import func

from backend.database.db import Base


class StudyPlan(Base):

    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(String)

    best_hour = Column(String)

    learning_health = Column(Float)

    productivity = Column(Float)

    burnout = Column(String)

    schedule = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )