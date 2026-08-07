import pandas as pd
import os
from datetime import datetime

FILE_NAME = "database/session_data.csv"


def save_record(
    attention_score,
    attention_state,
    emotion,
    fatigue,
    action
):

    record = pd.DataFrame({
        "timestamp": [datetime.now()],
        "attention_score": [attention_score],
        "attention_state": [attention_state],
        "emotion": [emotion],
        "fatigue": [fatigue],
        "action": [action]
    })

    if os.path.exists(FILE_NAME):

        record.to_csv(
            FILE_NAME,
            mode="a",
            header=False,
            index=False
        )

    else:

        record.to_csv(
            FILE_NAME,
            index=False
        )