from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from backend.database.db import Base


class ValidationLog(Base):

    __tablename__ = "validation_logs"

    id = Column(
        Integer,
        primary_key=True
    )

    request = Column(String)

    status = Column(String)

    reason = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )