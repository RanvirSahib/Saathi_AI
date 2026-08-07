from backend.database.db import SessionLocal
from backend.models.session_log import SessionLog

import pandas as pd


def get_dashboard_data():

    db = SessionLocal()

    try:

        records = db.query(SessionLog).all()

        data = []

        for record in records:

            data.append({

                "timestamp": record.timestamp,

                "attention_score": record.attention_score,

                "attention_state": record.attention_state,

                "emotion": record.emotion,

                "fatigue": record.fatigue,

                "action": record.action

            })

        df = pd.DataFrame(data)

        return df

    finally:

        db.close()