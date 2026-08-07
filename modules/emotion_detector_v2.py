import cv2
import torch
import timm
import mediapipe as mp

from PIL import Image
from torchvision import transforms

from collections import deque

emotion_history = deque(maxlen=20)
# --------------------------------------------------
# DEVICE
# --------------------------------------------------

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# --------------------------------------------------
# CLASS NAMES
# --------------------------------------------------

classes = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
]

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = timm.create_model(
    "efficientnet_b0",
    pretrained=False,
    num_classes=7
)

model.load_state_dict(
    torch.load(
        "models/emotion_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()

# --------------------------------------------------
# IMAGE TRANSFORM
# --------------------------------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean = [0.485,0.456,0.406],
        std = [0.229,0.224,0.225]
    )
])

# --------------------------------------------------
# MEDIAPIPE FACE DETECTOR
# --------------------------------------------------

mp_face_detection = mp.solutions.face_detection

face_detector = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

# --------------------------------------------------
# EMOTION PREDICTION
# --------------------------------------------------
def predict_emotion_from_frame(frame):

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = face_detector.process(rgb)

    if not results.detections:

        return (
            "No Face",
            0.0,
            None
        )

    detection = results.detections[0]

    bbox = (
        detection
        .location_data
        .relative_bounding_box
    )

    h, w, _ = frame.shape

    x = int(bbox.xmin * w)
    y = int(bbox.ymin * h)

    width = int(bbox.width * w)
    height = int(bbox.height * h)

    x = max(0, x)
    y = max(0, y)

    face = frame[
        y:y + height,
        x:x + width
    ]

    if face.size == 0:

        return (
            "No Face",
            0.0,
            None
        )

    image = cv2.cvtColor(
        face,
        cv2.COLOR_BGR2RGB
    )

    image = Image.fromarray(image)

    image = transform(image)

    image = image.unsqueeze(0)

    image = image.to(device)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

        confidence, prediction = torch.max(
            probabilities,
            dim=1
        )

    emotion = classes[
        prediction.item()
    ]

    confidence = confidence.item()

    # Confidence Threshold
    if confidence < 0.50:

        emotion = "neutral"

    # Add Emotion To History
    emotion_history.append(emotion)

    # Majority Voting
    stable_emotion = max(
        set(emotion_history),
        key=emotion_history.count
    )

    return (
        stable_emotion,
        confidence,
        (x, y, width, height)
    )

