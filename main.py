from studybuddyAIagent.user_profile import UserProfile
from studybuddyAIagent.knowledge_base import KnowledgeBase
from studybuddyAIagent.quiz_module import QuizModule
from studybuddyAIagent.chat_engine import simple_chatbot_response
from studybuddyAIagent.sensors import get_user_input
from actuators import respond

def main():
    print("Welcome to AI Study Buddy!")
    name = input("Enter your name: ")
    level = input("Enter your academic level: ")
    user = UserProfile(name, level)
    kb = KnowledgeBase()
    quiz = QuizModule()

    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif "quiz" in user_input.lower():
            topic = input("Enter quiz topic: ").lower()
            score = quiz.ask_quiz(topic)
            user.update_progress(topic, score)
            respond(f"You scored {score} out of {len(quiz.questions.get(topic, []))}.")
        else:
            response = simple_chatbot_response(user_input, kb)
            respond(response)

if __name__ == "__main__":
    main()
