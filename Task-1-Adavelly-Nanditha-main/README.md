# DecodeLabs AI Chatbot — Project 1
**Project Name:** Pure Rule-Based AI Chatbot (If-Else Logic Engine)  

---

## 📌 Project Overview
This project is part of the **DecodeLabs Industrial Training program (Project 1)**. 

It implements a pure rule-based chatbot using programmatic `if-elif-else` control flow logic. The application runs entirely within the terminal, requiring no web interfaces or external library dependencies.

---

## ⚙️ Features
1. **Pure Control Flow Logic**: All input matching is handled through sequential `if-elif-else` structures.
2. **Input Sanitization**: Handles case-insensitivity, trims leading/trailing whitespace, and strips trailing punctuation (`?`, `!`, `.`) to make matching resilient.
3. **Continuous Loop**: Runs in a continuous heartbeat loop until an exit command (`exit`, `bye`, `quit`, `goodbye`) is given.

---

## 📁 File Structure
```text
C:\Users\nandi\Documents\AI Project 1\
└── chatbot.py   # Pure Python Rule-Based Chatbot
```

---

## 🚀 How to Run the Chatbot

Since this chatbot is built purely with Python's standard library, it has no external dependencies.

1. Open your terminal or Command Prompt in the project directory.
2. Run the chatbot using Python:
   ```bash
   python chatbot.py
   ```

---

## 💬 Supported Dialogues

You can converse with the chatbot using various inputs:

| Category | Supported Inputs | Bot Response |
|---|---|---|
| **Greetings** | `hello`, `hi`, `hey`, `namaste`, `greetings` | Hello! Welcome to DecodeLabs. How can I help you today? |
| **Morning** | `good morning`, `morning` | Good morning! Welcome to DecodeLabs. |
| **Afternoon** | `good afternoon`, `afternoon` | Good afternoon! Welcome to DecodeLabs. |
| **Evening** | `good evening`, `evening` | Good evening! Welcome to DecodeLabs. |
| **Status Check** | `how are you`, `whats up`, etc. | I am fine, how are you? |
| **User Status** | `i am fine`, `fine`, `great`, etc. | That's wonderful to hear! |
| **AI Definition** | `what is ai`, `artificial intelligence`, etc. | Artificial Intelligence (AI) is the simulation of human intelligence by machines. |
| **ML Definition** | `what is ml`, `machine learning`, etc. | Machine Learning (ML) is a subset of AI where systems learn patterns from data. |
| **Python** | `what is python`, `python`, etc. | Python is a high-level programming language widely used in AI and software development. |
| **Chatbot** | `what is a chatbot`, `chatbot`, etc. | A chatbot is a software application that communicates with users through text or voice. |
| **Creator** | `who made you`, `creator`, etc. | I was created by a DecodeLabs AI Engineering Intern |
| **Joke** | `joke`, `tell me a joke`, etc. | (Picks a random joke from a list of 4 options, emoji-free) |
| **Fact** | `fact`, `fun fact`, etc. | (Picks a random fact from a list of 4 options, emoji-free) |
| **Thanks** | `thank you`, `thanks` | You're very welcome! Happy to help. |
| **Exit** | `exit`, `bye`, `quit`, `goodbye` | DecodeBot: Bye! Goodbye! |
