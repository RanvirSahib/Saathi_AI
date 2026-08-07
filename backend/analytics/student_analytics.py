import pandas as pd

from backend.analytics.learning_score import (
    calculate_learning_health_score
)

from backend.analytics.productivity import (
    productivity_analysis
)

from backend.analytics.trends import (
    weekly_trends
)


def get_student_analytics(df):

    if df.empty:

        return {

            "average_attention": 0,

            "learning_health": 0,

            "emotion": "Unknown",

            "fatigue": "Unknown",

            "focus_alerts": 0,

            "break_alerts": 0,

            "consistency": 0,

            "best_hour": None,

            "burnout": "Unknown",

            "productivity": 0,

            "trend": pd.DataFrame()

        }

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

    consistency = round(

        (len(df) / max(len(df), 1)) * 100,

        2

    )

    health = calculate_learning_health_score(

        avg_attention,

        emotion,

        fatigue,

        consistency

    )

    productivity = productivity_analysis(df)

    trend = weekly_trends(df)

    burnout = "Low"

    if fatigue == "Fatigued":

        burnout = "Medium"

    if fatigue == "Drowsy":

        burnout = "High"

    return {

        "average_attention": avg_attention,

        "learning_health": health,

        "emotion": emotion,

        "fatigue": fatigue,

        "focus_alerts": focus_alerts,

        "break_alerts": break_alerts,

        "consistency": consistency,

        "best_hour": productivity["best_hour"],

        "productivity": productivity["average_attention"],

        "burnout": burnout,

        "trend": trend

    }