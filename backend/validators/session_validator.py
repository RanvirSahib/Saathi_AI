VALID_EMOTIONS = [
    "happy",
    "neutral",
    "sad",
    "angry",
    "fear",
    "surprise",
    "disgust"
]

VALID_FATIGUE = [
    "Normal",
    "Fatigued",
    "Drowsy"
]

VALID_ACTIONS = [
    "NONE",
    "FOCUS",
    "BREAK",
    "SUPPORT",
    "GUIDANCE"
]


def validate_session(
    attention_score,
    attention_state,
    emotion,
    fatigue,
    action
):

    errors = []

    if not 0 <= attention_score <= 100:
        errors.append("Attention score must be between 0 and 100.")

    if attention_state == "":
        errors.append("Attention state cannot be empty.")

    if emotion.lower() not in VALID_EMOTIONS:
        errors.append("Invalid emotion detected.")

    if fatigue not in VALID_FATIGUE:
        errors.append("Invalid fatigue state.")

    if action not in VALID_ACTIONS:
        errors.append("Invalid AI action.")

    return {

        "valid": len(errors) == 0,

        "errors": errors

    }