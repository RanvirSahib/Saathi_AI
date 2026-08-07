import os
from google import genai

from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_saathi_response(
    attention_state,
    attention_score,
    fatigue_state,
    emotion_state
):
    

    prompt = prompt = f"""
You are Saathi, an AI-powered study companion.

Current student information:

Attention State: {attention_state}
Attention Score: {attention_score}
Fatigue State: {fatigue_state}
Emotion State: {emotion_state}


Instructions:
1. Analyze the student's condition.
2. Explain WHY the condition may be occurring.
3. Give one practical study recommendation.
4. Do NOT always suggest taking a break.
5. If attention is good, encourage continued study.
6. If frustration is detected, suggest a learning strategy.
8. Sound like a academic mentor, not a therapist.
9. Keep the response under 30 words.
10. Give the response in simple language.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text