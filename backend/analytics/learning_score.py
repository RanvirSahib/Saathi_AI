def calculate_learning_health_score(
    average_attention,
    emotion,
    fatigue,
    consistency
):

    score = average_attention * 0.60

    if emotion in ["happy", "neutral"]:
        score += 20
    else:
        score += 10

    if fatigue == "Normal":
        score += 10
    elif fatigue == "Fatigued":
        score += 5

    score += consistency * 0.10

    return round(min(score, 100), 2)