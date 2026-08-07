

import os
from google import genai

from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_study_plan(
    average_attention,
    learning_health,
    emotion,
    fatigue,
    best_hour
):

    prompt = f"""

You are Saathi AI.

Student Analytics

Average Attention : {average_attention}

Learning Health Score : {learning_health}

Emotion : {emotion}

Fatigue : {fatigue}

Most Productive Hour : {best_hour}

Create tomorrow's study schedule.

Rules

Include

Study Blocks

Breaks

Revision

Practice Questions

Motivation

Keep response below 180 words.

"""

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt

    )

    return response.text