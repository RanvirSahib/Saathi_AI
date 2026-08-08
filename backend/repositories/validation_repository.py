from backend.database.db import SessionLocal
from backend.models.validation_log import ValidationLog


def save_validation(
    request,
    status,
    reason
):

    db = SessionLocal()

    try:

        record = ValidationLog(

            request=request,

            status=status,

            reason=reason

        )

        db.add(record)

        db.commit()

    finally:

        db.close()