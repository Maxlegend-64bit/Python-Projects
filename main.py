import json
import os

data_file = "knowledge.json"

# Load existing knowledge from file
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        knowledge = json.load(file)
else:
    knowledge = {}

def save_data():
    with open(data_file, "w") as file:
        json.dump(knowledge, file)

def ai(question):
    question = question.lower()
    if question in knowledge:
        answer = knowledge[question]
        print("AI:", answer)
    else:
        # Call your external module's AI function
        answer = input("AI: I don't know. Can you teach me? ")
        knowledge[question] = answer
        save_data()
        print("AI: Got it! I’ll remember that.")

# 🔁 Chat Loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye!")
        break
    ai(user_input)