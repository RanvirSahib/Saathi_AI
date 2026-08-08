import cv2
import time
import threading

from backend.services.session_service import save_record

from modules.attention_monitor_v2 import (
    detect_attention
)

from modules.fatigue_v2 import (
    detect_fatigue
)

from modules.emotion_detector_v2 import (
    predict_emotion_from_frame
)

from modules.decision_engine import (
    decision_engine
)

from modules.saathi_assistant import (
    generate_saathi_response
)

from modules.text_to_speech import speak

from backend.services.job_service import (
    start_analysis_job,
    finish_analysis_job
)



last_ai_time = 0

AI_INTERVAL = 30

last_save_time = 0

SAVE_INTERVAL = 5


ai_busy = False

last_response = ""  

job_id = start_analysis_job()

def get_ai_response(
    attention_state,
    attention_score,
    fatigue_state,
    emotion
):

    global ai_response
    global ai_busy
    global last_response

    try:

        ai_response = generate_saathi_response(
            attention_state,
            attention_score,
            fatigue_state,
            emotion
        )

        print("\nSaathi:")
        print(ai_response)


        if ai_response != last_response:

            threading.Thread(
                target=speak,
                args=(ai_response,),
                daemon=True
            ).start()

            last_response = ai_response

    except Exception as e:

        print("Gemini Error:", e)

    ai_busy = False



cap = cv2.VideoCapture(0)

while True:
    

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    # -------------------------
    # ATTENTION
    # -------------------------

    (
        attention_state,
        attention_score,
        gaze,
        head_pose
    ) = detect_attention(frame)

    # -------------------------
    # FATIGUE
    # -------------------------

    fatigue_state, ear = (
        detect_fatigue(frame)
    )

    # -------------------------
    # EMOTION
    # -------------------------

    (
        emotion,
        confidence,
        box
    ) = predict_emotion_from_frame(frame)

    # -------------------------
    # Decision Engine
    # -------------------------

    decision = decision_engine(
        attention_state,
        attention_score,
        fatigue_state,
        emotion
    )

    action = decision["action"]
    message = decision["message"]


    # -------------------------
    # Session Logger
    # -------------------------

    current_time = time.time()

    if current_time - last_save_time > SAVE_INTERVAL:

        save_record(
            attention_score,
            attention_state,
            emotion,
            fatigue_state,
            action
        )

        last_save_time = current_time

    # -------------------------
    # Assistant
    # -------------------------
    important_actions = [
        "FOCUS",
        "BREAK",
        "SUPPORT",
        "GUIDANCE"
    ]

    current_time = time.time()

    if action in important_actions:

        if current_time - last_ai_time > AI_INTERVAL:

            if not ai_busy:

                ai_busy = True

                threading.Thread(
                    target=get_ai_response,
                    args=(
                        attention_state,
                        attention_score,
                        fatigue_state,
                        emotion
                    ),
                    daemon=True
                ).start()

                last_ai_time = current_time

    # -------------------------
    # DISPLAY
    # -------------------------


    cv2.putText(
        frame,
        f"Attention: {attention_state}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Score: {attention_score}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Fatigue: {fatigue_state}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Action: {action}",
        (20, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )
    
    # cv2.putText(
    #     frame,
    #     ai_response[:60],
    #     (20, 240),
    #     cv2.FONT_HERSHEY_SIMPLEX,
    #     0.5,
    #     (255,255,255),
    #     1
    # )


    cv2.imshow(
        "Saathi AI",
        frame
    )


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

finish_analysis_job(job_id)