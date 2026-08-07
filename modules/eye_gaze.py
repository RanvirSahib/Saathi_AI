import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    h, w, _ = frame.shape

    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]
    
        # Left eye corners
        left_corner = face_landmarks.landmark[33]
        right_corner = face_landmarks.landmark[133]

        # Iris center
        iris = face_landmarks.landmark[468]

        left_x = int(left_corner.x * w)
        right_x = int(right_corner.x * w)
        iris_x = int(iris.x * w)

        eye_width = right_x - left_x

        if eye_width != 0:

            ratio = (iris_x - left_x) / eye_width

            if ratio < 0.40:
                gaze = "Looking Left"

            elif ratio > 0.60:
                gaze = "Looking Right"

            else:
                gaze = "Looking Center"

            cv2.putText(
                frame,
                gaze,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.imshow("Eye Gaze Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()