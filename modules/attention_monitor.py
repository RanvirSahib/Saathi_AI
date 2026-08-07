import cv2
import mediapipe as mp
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

distraction_start = None

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    h, w, _ = frame.shape

    attention_state = "No Face"
    attention_score = 0

    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]

        # -------------------------
        # EYE GAZE DETECTION
        # -------------------------

        left_corner = face_landmarks.landmark[33]
        right_corner = face_landmarks.landmark[133]
        iris = face_landmarks.landmark[468]

        left_x = int(left_corner.x * w)
        right_x = int(right_corner.x * w)
        iris_x = int(iris.x * w)

        eye_width = right_x - left_x

        gaze = "Unknown"

        if eye_width != 0:

            ratio = (iris_x - left_x) / eye_width

            if ratio < 0.40:
                gaze = "Left"

            elif ratio > 0.60:
                gaze = "Right"

            else:
                gaze = "Center"

        # -------------------------
        # HEAD POSE DETECTION
        # -------------------------

        face_2d = []
        face_3d = []

        selected_points = [33, 263, 1, 61, 291, 199]

        for idx in selected_points:

            lm = face_landmarks.landmark[idx]

            x = int(lm.x * w)
            y = int(lm.y * h)

            face_2d.append([x, y])
            face_3d.append([x, y, lm.z])

        face_2d = np.array(face_2d, dtype=np.float64)
        face_3d = np.array(face_3d, dtype=np.float64)

        focal_length = w

        cam_matrix = np.array([
            [focal_length, 0, w / 2],
            [0, focal_length, h / 2],
            [0, 0, 1]
        ])

        dist_matrix = np.zeros((4, 1))

        success, rot_vec, trans_vec = cv2.solvePnP(
            face_3d,
            face_2d,
            cam_matrix,
            dist_matrix
        )

        rmat, _ = cv2.Rodrigues(rot_vec)

        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)

        x_angle = angles[0] * 360
        y_angle = angles[1] * 360

        # cv2.putText(
        #     frame,
        #     f"X:{x_angle:.2f}",
        #     (20, 200),
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     0.7,
        #     (255, 255, 255),
        #     2
        # )

        # cv2.putText(
        #     frame,
        #     f"Y:{y_angle:.2f}",
        #     (20, 230),
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     0.7,
        #     (255, 255, 255),
        #     2
        # )
        head_pose = "Straight"

        if y_angle < -10:
            head_pose = "Left"

        elif y_angle > 10:
            head_pose = "Right"

        elif x_angle > 15:
            head_pose = "Up"

        elif x_angle < -5:
            head_pose = "Down"

        else:
            head_pose = "Straight"

        # -------------------------
        # ATTENTION CLASSIFICATION
        # -------------------------

        if head_pose == "Down":

            attention_state = "Focused (Notebook)"
            attention_score = 90
            distraction_start = None

        elif gaze == "Center" and head_pose == "Straight":

            attention_state = "Focused"
            attention_score = 100
            distraction_start = None

        else:

            if distraction_start is None:
                distraction_start = time.time()

            distracted_time = time.time() - distraction_start

            if distracted_time > 3:

                attention_state = "Distracted"
                attention_score = 40

            else:

                attention_state = "Monitoring..."
                attention_score = 70

        # -------------------------
        # DISPLAY
        # -------------------------

        cv2.putText(
            frame,
            f"Gaze: {gaze}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Head: {head_pose}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"State: {attention_state}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Score: {attention_score}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

    cv2.imshow("Saathi - Attention Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()