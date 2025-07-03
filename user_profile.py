class UserProfile:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.topics_learned = []
        self.quiz_scores = {}

    def update_progress(self, topic, score):
        self.topics_learned.append(topic)
        self.quiz_scores[topic] = score
