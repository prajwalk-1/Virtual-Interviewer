def get_questions(domain):
    question_sets = {
        "General": ["Tell me about yourself.", "What are your strengths and weaknesses?"],
        "Technical": ["Explain polymorphism in OOP.", "What is the time complexity of a binary search?"],
        "HR": ["Why do you want this job?", "How do you handle workplace conflict?"],
        "Management": ["Describe your leadership style.", "How do you prioritize tasks under pressure?"]
    }
    return question_sets.get(domain, [])
