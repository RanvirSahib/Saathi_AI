def decision_engine(attention_state,
                    attention_score,
                    fatigue_state,
                    emotion_state):

    # Fatigue has highest priority

    if fatigue_state == "Drowsy":

        return {
            "action": "BREAK",
            "message":
            "You appear very tired. Please take a 10-minute break."
        }

    if fatigue_state == "Fatigued":

        return {
            "action": "BREAK",
            "message":
            "You seem tired. Consider taking a short break."
        }

    # Attention

    if attention_state == "Distracted":

        return {
            "action": "FOCUS",
            "needs_ai": True,
            "message":
            "Your attention seems to be drifting. Let's refocus on the task."
        }

    # Emotion

    if emotion_state == "Sad":

        return {
            "action": "SUPPORT",
            "message":
            "Don't worry. Learning takes time. Keep moving forward."
        }

    if emotion_state == "Frustrated":

        return {
            "action": "SUPPORT",
            "message":
            "This topic may be difficult, but you are making progress."
        }

    if emotion_state == "Confused":

        return {
            "action": "GUIDANCE",
            "message":
            "Try breaking the problem into smaller steps."
        }

    # Positive state

    if attention_score >= 90:

        return {
            "action": "NONE",
            "message":
            "Excellent focus. Keep up the good work."
        }

    return {
        "action": "NONE",
        "needs_ai": False,
        "message":
        "Continue studying."
    }