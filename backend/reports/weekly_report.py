from backend.analytics.learning_score import (
    calculate_learning_health_score
)


def generate_weekly_report(df):

    avg_attention = round(

        df["attention_score"].mean(),

        2

    )

    emotion = (

        df["emotion"]

        .mode()[0]

    )

    fatigue = (

        df["fatigue"]

        .mode()[0]

    )

    focus_alerts = len(

        df[df["action"] == "FOCUS"]

    )

    break_alerts = len(

        df[df["action"] == "BREAK"]

    )

    consistency = 90

    health = calculate_learning_health_score(

        avg_attention,

        emotion,

        fatigue,

        consistency

    )

    recommendation = []

    if avg_attention > 90:

        recommendation.append(

            "Maintain your current study routine."

        )

    else:

        recommendation.append(

            "Reduce distractions during study sessions."

        )

    if fatigue != "Normal":

        recommendation.append(

            "Take short breaks every hour."

        )

    return {

        "Average Attention": avg_attention,

        "Emotion": emotion,

        "Fatigue": fatigue,

        "Focus Alerts": focus_alerts,

        "Break Alerts": break_alerts,

        "Learning Health Score": health,

        "Recommendations": recommendation

    }