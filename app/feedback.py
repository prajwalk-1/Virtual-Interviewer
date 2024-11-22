def generate_feedback(scores):
    avg_score = sum(scores) / len(scores)
    if avg_score > 8:
        return ["Great job! Keep refining your skills."]
    elif avg_score > 5:
        return ["Work on elaborating your answers.", "Focus on key details in your responses."]
    else:
        return ["Practice answering common questions.", "Improve clarity and confidence."]
