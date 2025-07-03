def simple_chatbot_response(user_input, kb):
    if "explain" in user_input.lower():
        topic = user_input.lower().replace("explain", "").strip()
        return kb.get_explanation(topic)
    elif "quiz" in user_input.lower():
        return "Sure! Let's start a quiz. Type the topic."
    else:
        return "I'm still learning. Try asking for an explanation or quiz."
