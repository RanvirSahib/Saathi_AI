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

closed_frames = 0

EAR_THRESHOLD = 0.175
FATIGUE_FRAMES = 15
DROWSY_FRAMES = 40


def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def detect_fatigue(frame):

    global closed_frames

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    h, w, _ = frame.shape

    fatigue_state = "Normal"
    ear = 0.0

    if results.multi_face_landmarks:

        landmarks = results.multi_face_landmarks[0].landmark

        left_eye = [33, 160, 158, 133, 153, 144]

        points = []

        for idx in left_eye:

            x = int(landmarks[idx].x * w)
            y = int(landmarks[idx].y * h)

            points.append((x, y))

        A = euclidean_distance(points[1], points[5])
        B = euclidean_distance(points[2], points[4])
        C = euclidean_distance(points[0], points[3])

        ear = (A + B) / (2.0 * C)

        if ear < EAR_THRESHOLD:
            closed_frames += 1
        else:
            closed_frames = 0

        if closed_frames > DROWSY_FRAMES:
            fatigue_state = "Drowsy"

        elif closed_frames > FATIGUE_FRAMES:
            fatigue_state = "Fatigued"

    return fatigue_state, ear