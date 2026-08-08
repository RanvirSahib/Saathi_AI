from backend.repositories.session_repository import save_session

from backend.validators.session_validator import (
    validate_session
)

from backend.services.validation_service import (
    log_validation
)

from backend.services.audit_service import log_event

log_event(

    role="Student",

    action="Session Saved",

    resource="Session Log"

)

def save_record(
    attention_score,
    attention_state,
    emotion,
    fatigue,
    action
):
    result = validate_session(

        attention_score,

        attention_state,

        emotion,

        fatigue,

        action

    )

    log_validation(

        "Session",

        result

    )

    if not result["valid"]:

        return

    save_session(

        attention_score,

        attention_state,

        emotion,

        fatigue,

        action

    )