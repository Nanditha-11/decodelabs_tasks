import random

print("=" * 10)
print(" CHATBOT ")
print("=" * 10)
print("Type 'help' for options or 'exit' to quit.")
print("-" * 50)

while True:
    user = input("You: ").lower().strip().rstrip("?.!")

    if not user:
        continue

    if user in ["exit", "bye", "quit", "goodbye"]:
        print("DecodeBot: Bye! Goodbye!")
        break

    elif user in ["hello", "hi", "hey", "namaste", "greetings"]:
        print("DecodeBot: Hello! Welcome to DecodeLabs. How can I help you today?")

    elif user in ["good morning", "morning"]:
        print("DecodeBot: Good morning! Welcome to DecodeLabs.")

    elif user in ["good afternoon", "afternoon"]:
        print("DecodeBot: Good afternoon! Welcome to DecodeLabs.")

    elif user in ["good evening", "evening"]:
        print("DecodeBot: Good evening! Welcome to DecodeLabs.")

    elif user in [
        "how are you",
        "how are you doing",
        "whats up",
        "hows it going",
        "how you doing"
    ]:
        print("DecodeBot: I am fine, how are you?")

    elif user in [
        "i am fine",
        "im fine",
        "i'm fine",
        "fine",
        "great",
        "awesome",
        "doing well"
    ]:
        print("DecodeBot: That's wonderful to hear!")

    elif user in [
        "what is ai",
        "artificial intelligence",
        "explain ai",
        "define ai",
        "tell me about ai"
    ]:
        print("DecodeBot: Artificial Intelligence (AI) is the simulation of human intelligence by machines.")

    elif user in [
        "what is ml",
        "machine learning",
        "explain machine learning",
        "define ml"
    ]:
        print("DecodeBot: Machine Learning (ML) is a subset of AI where systems learn patterns from data.")

    elif user in [
        "what is python",
        "python",
        "tell me about python",
        "python language"
    ]:
        print("DecodeBot: Python is a high-level programming language widely used in AI and software development.")

    elif user in [
        "what is a chatbot",
        "chatbot",
        "chat bot",
        "what is a bot"
    ]:
        print("DecodeBot: A chatbot is a software application that communicates with users through text or voice.")

    elif user in [
        "who made you",
        "who created you",
        "who built you",
        "your creator",
        "your developer"
    ]:
        print("DecodeBot: I was created by a DecodeLabs AI Engineering Intern ")

    elif user in [
        "tell me a joke",
        "joke",
        "something funny",
        "make me laugh"
    ]:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "Why did the programmer quit their job? Because they didn't get arrays!"
        ]
        print("DecodeBot:", random.choice(jokes))

    elif user in [
        "fun fact",
        "fact",
        "did you know",
        "tell me a fact"
    ]:
        facts = [
            "The first computer bug was an actual moth found trapped in a relay in 1947!",
            "The first computer programmer was Ada Lovelace, a woman who wrote an algorithm for Charles Babbage's Analytical Engine in 1843!",
            "The first electronic computer, ENIAC, weighed more than 27 tons and took up 1,800 square feet!",
            "Python was named after the British comedy troupe 'Monty Python', not the snake!"
        ]
        print("DecodeBot:", random.choice(facts))

    elif user in [
        "thank you",
        "thanks",
        "thank you so much"
    ]:
        print("DecodeBot: You're very welcome! Happy to help.")

    else:
        print("DecodeBot: I'm not sure how to respond to that.")
