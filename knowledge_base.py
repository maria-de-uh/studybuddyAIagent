import json

class KnowledgeBase:
    def __init__(self, path='data/topics.json'):
        with open(path, 'r') as file:
            self.topics = json.load(file)

    def get_explanation(self, topic):
        return self.topics.get(topic.lower(), "Sorry, I don't know that yet.")
