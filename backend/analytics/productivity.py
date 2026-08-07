import pandas as pd


def productivity_analysis(df):

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["hour"] = df["timestamp"].dt.hour

    best_hour = (
        df.groupby("hour")["attention_score"]
        .mean()
        .idxmax()
    )

    return {

        "best_hour": best_hour,

        "average_attention":

        round(
            df["attention_score"].mean(),
            2
        )

    }