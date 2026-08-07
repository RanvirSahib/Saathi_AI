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

cap = cv2.VideoCapture(0)


def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    h, w, _ = frame.shape

    fatigue_state = "Normal"

    if results.multi_face_landmarks:

        landmarks = results.multi_face_landmarks[0].landmark

        # Left eye landmarks
        left_eye = [33, 160, 158, 133, 153, 144]

        points = []

        for idx in left_eye:

            x = int(landmarks[idx].x * w)
            y = int(landmarks[idx].y * h)

            points.append((x, y))

            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # EAR calculation
        A = euclidean_distance(points[1], points[5])
        B = euclidean_distance(points[2], points[4])
        C = euclidean_distance(points[0], points[3])

        EAR = (A + B) / (2.0 * C)

        # Display EAR
        cv2.putText(
            frame,
            f"EAR: {EAR:.2f}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Eye closure tracking
        if EAR < EAR_THRESHOLD:
            closed_frames += 1
        else:
            closed_frames = 0

        # Fatigue classification
        if closed_frames > DROWSY_FRAMES:
            fatigue_state = "Drowsy"

        elif closed_frames > FATIGUE_FRAMES:
            fatigue_state = "Fatigued"

        else:
            fatigue_state = "Normal"

    # Display state
    cv2.putText(
        frame,
        f"State: {fatigue_state}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("Fatigue Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()