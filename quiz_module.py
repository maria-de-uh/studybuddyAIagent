class QuizModule:
    def __init__(self):
        self.questions = {
            "python loops": [
                {"q": "What loop repeats while a condition is true?", "a": "while"},
                {"q": "Which loop is best for iterating a list?", "a": "for"}
            ]
        }

    def ask_quiz(self, topic):
        score = 0
        if topic not in self.questions:
            print("No quiz available.")
            return score
        for q in self.questions[topic]:
            answer = input(q['q'] + " ")
            if answer.strip().lower() == q['a']:
                score += 1
        return score
