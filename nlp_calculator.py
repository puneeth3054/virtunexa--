import logging
from textblob import TextBlob
import os

# === Setup Logging ===
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Calculator Function ===
def perform_calculation():
    print("\n==== Calculator ====")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                logging.warning("Attempted division by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            logging.warning("Invalid operator used.")
            return

        print(f"Result: {result}")
        logging.info(f"Calculator: {num1} {op} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        logging.warning("Invalid numeric input.")

# === Sentiment Analysis Function ===
def analyze_sentiment():
    print("\n==== Sentiment Analysis ====")
    text = input("Enter text to analyze: ")
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity:.2f}")
    print(f"Subjectivity: {subjectivity:.2f}")
    logging.info(f"Sentiment: '{text}' => {sentiment} (Polarity: {polarity}, Subjectivity: {subjectivity})")

# === Main Menu ===
def show_menu():
    print("\n==== NLP + Calculator Tool ====")
    print("1. Calculator")
    print("2. Sentiment Analysis")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            perform_calculation()
        elif choice == "2":
            analyze_sentiment()
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Try again.")

# === Entry Point ===
if __name__ == "__main__":
    main()
