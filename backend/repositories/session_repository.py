from backend.database.db import SessionLocal
from backend.models.session_log import SessionLog


def save_session(
    attention_score,
    attention_state,
    emotion,
    fatigue,
    action
):

    db = SessionLocal()

    try:

        record = SessionLog(

            attention_score=attention_score,

            attention_state=attention_state,

            emotion=emotion,

            fatigue=fatigue,

            action=action

        )

        db.add(record)

        db.commit()

    finally:

        db.close()