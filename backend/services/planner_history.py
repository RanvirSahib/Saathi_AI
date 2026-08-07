from backend.database.db import SessionLocal
from backend.models.study_plan import StudyPlan


def get_latest_plan():

    db = SessionLocal()

    try:

        return (
            db.query(StudyPlan)
            .order_by(StudyPlan.created_at.desc())
            .first()
        )

    finally:

        db.close()