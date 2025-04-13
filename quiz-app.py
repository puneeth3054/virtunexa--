import random
import logging
import os

# === Logging Setup ===
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/quiz.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Sample Question Bank ===
questions = [
    {"question": "What is the capital of France?", "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"], "answer": "C"},
    {"question": "What is 5 + 7?", "options": ["A) 12", "B) 10", "C) 11", "D) 13"], "answer": "A"},
    {"question": "What is the largest planet?", "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"], "answer": "B"},
    {"question": "Which language is used for web apps?", "options": ["A) Python", "B) Java", "C) JavaScript", "D) C++"], "answer": "C"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A) Dickens", "B) Chaucer", "C) Tolkien", "D) Shakespeare"], "answer": "D"}
]

# === Quiz Logic ===
def run_quiz():
    print("=== Welcome to the Random Quiz! ===")
    selected_questions = random.sample(questions, k=3)
    score = 0

    for idx, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
            logging.info(f"Question: {q['question']} | User answered correctly.")
        else:
            print(f"❌ Incorrect. Correct answer is: {q['answer']}")
            logging.info(f"Question: {q['question']} | User answered: {answer} | Correct: {q['answer']}")

    print(f"\n🎯 Your final score: {score} / {len(selected_questions)}")
    logging.info(f"Quiz completed with score: {score} / {len(selected_questions)}")

# === Entry Point ===
if __name__ == "__main__":
    run_quiz()
