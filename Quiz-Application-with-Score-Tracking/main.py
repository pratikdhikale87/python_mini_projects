import requests
import random
import html

API_URL = "https://opentdb.com/api.php?amount=5&type=multiple"

def fetch_questions():
    response = requests.get(API_URL)
    data = response.json()
    return data["results"]

def run_quiz(questions):
    score = 0

    for index, q in enumerate(questions, start=1):
        question = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in q["incorrect_answers"]]

        options = incorrect_answers + [correct_answer]
        random.shuffle(options)

        print(f"\nQuestion {index}: {question}")

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Your answer (number): "))
            selected_option = options[user_choice - 1]

            if selected_option == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {correct_answer}")

        except (ValueError, IndexError):
            print("Invalid input. Question skipped.")

    return score


print(" Welcome to the Trivia Quiz!")
questions = fetch_questions()
total = len(questions)

score = run_quiz(questions)

print("\nQuiz Completed!")
print(f"Score: {score}/{total}")
print(f"Percentage: {(score / total) * 100:.2f}%")


