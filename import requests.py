print("welcome to the quiz game")
name=input("what is your name?")
print("hello " + name)


def quiz_game(questions, answers):
    score = 0  # Start with 0 points

    for i in range(len(questions)):  # For each question
        print(questions[i])  # Show question
        user_answer = input("Your answer: ")  # Ask for input

        if user_answer.lower() == answers[i].lower():  # Check answer
            print("Correct!\n")
            score += 1  # Add 1 point
        else:
            print("Wrong!\n")

    print("You got", score, "out of", len(questions))  # Final score


# List of questions and correct answers
questions = ["What is 10+(7-2)?", "What is the capital of France?", "what is the tallest mountain","who is the god in bible"]
answers = ["15", "Paris","mt everest", "JESUS"]

# Run the quiz
quiz_game(questions, answers)
