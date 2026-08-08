from backend.database.db import SessionLocal
from backend.models.audit_log import AuditLog

def save_audit(role, action, resource, status):

    db = SessionLocal()

    try:

        log = AuditLog(

            role=role,

            action=action,

            resource=resource,

            status=status

        )

        db.add(log)

        db.commit()

    finally:

        db.close()