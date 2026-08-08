from backend.repositories.audit_repository import save_audit

def log_event(
    role,
    action,
    resource,
    status="SUCCESS"
):

    save_audit(

        role,

        action,

        resource,

        status

    )