import speech_recognition as sr
from googletrans import Translator
import logging
import os

# === Logging Setup ===
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/translator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

translator = Translator()

# === Speech-to-Text Function ===
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 You said: {text}")
        logging.info(f"Recognized speech: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech not recognized.")
        logging.warning("Speech not recognized.")
    except sr.RequestError:
        print("Could not request results.")
        logging.error("Speech recognition API request failed.")
    return None

# === Translation Function ===
def translate_text(text, dest_lang='es'):
    try:
        translated = translator.translate(text, dest=dest_lang)
        print(f"🌍 Translated to [{dest_lang}]: {translated.text}")
        logging.info(f"Translated '{text}' to '{translated.text}' [{dest_lang}]")
    except Exception as e:
        print("Translation failed.")
        logging.error(f"Translation error: {e}")

# === Main Interface ===
def main():
    print("=== Multilingual Translator with Speech Support ===")
    while True:
        print("\n1. Translate typed text")
        print("2. Translate speech")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter text to translate: ")
            lang = input("Enter target language code (e.g., 'fr', 'de', 'es'): ").strip().lower()
            translate_text(text, lang)
        elif choice == "2":
            lang = input("Enter target language code (e.g., 'fr', 'de', 'es'): ").strip().lower()
            speech_text = recognize_speech()
            if speech_text:
                translate_text(speech_text, lang)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
