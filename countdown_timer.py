import time
import threading
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='timer_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_timer(duration, unit):
    message = f"Started a countdown for {duration} {unit}"
    logging.info(message)

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {timer_display}", end='', flush=True)
        time.sleep(1)
        seconds -= 1
    print("\n🚨 Time's up!")

def start_timer():
    print("===== Countdown Timer =====")
    try:
        choice = input("Set time in (m)inutes or (s)econds? [m/s]: ").strip().lower()
        if choice == 'm':
            minutes = float(input("Enter minutes: "))
            total_seconds = int(minutes * 60)
            log_timer(minutes, "minutes")
        elif choice == 's':
            seconds = float(input("Enter seconds: "))
            total_seconds = int(seconds)
            log_timer(seconds, "seconds")
        else:
            print("❌ Invalid choice. Please enter 'm' or 's'.")
            return

        print(f"▶️ Countdown started for {total_seconds} seconds...")
        timer_thread = threading.Thread(target=countdown, args=(total_seconds,))
        timer_thread.start()
        timer_thread.join()

    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    start_timer()
