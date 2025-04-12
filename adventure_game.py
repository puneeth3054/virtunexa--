import logging

# Logging setup
logging.basicConfig(filename='game_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Global inventory
inventory = []

def intro():
    print("\n🌄 Welcome, adventurer!")
    print("You awaken in a dark forest with two paths.")
    logging.info("Game started.")
    choose_path()

def choose_path():
    print("\nDo you:")
    print("1. Take the left path 🛤️")
    print("2. Take the right path 🌲")

    choice = input("Enter 1 or 2: ").strip()
    
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Try again.")
        choose_path()

def left_path():
    print("\nYou find a shimmering sword on the ground.")
    inventory.append("Sword")
    logging.info("Player found a Sword.")
    print("You pick up the sword and continue forward.")

    dragon_encounter()

def right_path():
    print("\nYou encounter a mysterious stranger who gives you a healing potion.")
    inventory.append("Potion")
    logging.info("Player received a Potion.")
    print("You thank them and move ahead.")
    
    dragon_encounter()

def dragon_encounter():
    print("\n🔥 A dragon blocks your way!")
    print("You can choose to:")
    print("1. Fight the dragon")
    print("2. Run away")

    choice = input("What do you do? Enter 1 or 2: ").strip()
    
    if choice == '1':
        if "Sword" in inventory:
            print("🗡️ You slay the dragon with your sword! You win!")
            logging.info("Player defeated the dragon.")
        else:
            print("You try to fight, but you have no weapon... The dragon wins.")
            logging.info("Player was defeated by the dragon.")
    elif choice == '2':
        print("You escape safely... but the adventure is over.")
        logging.info("Player ran from the dragon.")
    else:
        print("Invalid choice. Try again.")
        dragon_encounter()

def main():
    while True:
        intro()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! 🏕️")
            break

if __name__ == "__main__":
    main()
