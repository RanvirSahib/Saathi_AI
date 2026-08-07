from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from backend.database.db import Base


class SessionLog(Base):

    __tablename__ = "session_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    attention_score = Column(
        Float,
        nullable=False
    )

    attention_state = Column(
        String,
        nullable=False
    )

    emotion = Column(
        String,
        nullable=False
    )

    fatigue = Column(
        String,
        nullable=False
    )

    action = Column(
        String,
        nullable=False
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )