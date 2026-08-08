from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from backend.database.db import Base


class AnalysisJob(Base):

    __tablename__ = "analysis_jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    job_name = Column(String)

    status = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    error = Column(String)