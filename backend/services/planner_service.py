from backend.database.db import SessionLocal
from backend.models.study_plan import StudyPlan
from backend.services.audit_service import log_event


def save_plan(
    date,
    best_hour,
    learning_health,
    productivity,
    burnout,
    schedule
):

    db = SessionLocal()

    try:

        plan = StudyPlan(
            date=date,
            best_hour=str(best_hour),
            learning_health=learning_health,
            productivity=productivity,
            burnout=burnout,
            schedule=schedule
        )

        db.add(plan)
        db.commit()

    finally:
        db.close()

log_event(

    role="Student",

    action="Study Plan Generated",

    resource="Study Planner"

)

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