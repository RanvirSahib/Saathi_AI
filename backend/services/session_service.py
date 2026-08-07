from backend.repositories.session_repository import save_session


def save_record(
    attention_score,
    attention_state,
    emotion,
    fatigue,
    action
):

    save_session(

        attention_score,

        attention_state,

        emotion,

        fatigue,

        action

    )