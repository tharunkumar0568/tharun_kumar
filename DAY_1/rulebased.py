def input_validation(text):
    return text.strip().lower()


def intent_detection(text):
    if "price" in text:
        return "price"
    elif "hello" in text:
        return "greet"
    elif "bye" in text:
        return "exit"
    else:
        return "unknown"


def knowledge_base(intent):
    data = {
        "price": "Product price is $100",
        "greet": "How can I help you?",
        "exit": "Have a good day",
        "unknown": "Sorry, I don't understand that"
    }
    return data[intent]


def ai_processing(response):
    return response


def chatbot_workflow(user_input):
    step1 = input_validation(user_input)
    step2 = intent_detection(step1)
    step3 = knowledge_base(step2)
    step4 = ai_processing(step3)
    return step4


while True:
    user = input("You: ")
    bot = chatbot_workflow(user)
    print("Bot:", bot)

    if "bye" in user.lower():
        break
