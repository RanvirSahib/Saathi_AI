import pandas as pd


def weekly_trends(df):

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["date"] = df["timestamp"].dt.date

    trend = (

        df.groupby("date")

        ["attention_score"]

        .mean()

        .reset_index()

    )

    return trend