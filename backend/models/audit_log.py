from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from backend.database.db import Base

class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    role = Column(String)

    action = Column(String)

    resource = Column(String)

    status = Column(String)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )