from backend.database.db import Base
from backend.database.db import engine

from backend.models.user import User
from backend.models.session_log import SessionLog
from backend.models.study_plan import StudyPlan

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Done!")