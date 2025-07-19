import random
import time

# ------------------ Constants ------------------ #
def default_choices():
    return ["snake", "water", "gun"]

# ------------------ Computer Choice ------------------ #
def generate_random_choice():
    print("Computer is thinking...")
    time.sleep(1)
    return random.choice(default_choices())

# ------------------ User Input for Each Round ------------------ #
def get_valid_user_choice(user_name):
    user_choice = input(f"Hey! {user_name}, Enter your choice (Snake / Water / Gun): ").strip().lower()
    while user_choice not in default_choices():
        print(f"{user_name}, this is an invalid choice! Please choose snake, water, or gun.")
        user_choice = input("Please enter your choice (Snake / Water / Gun): ").strip().lower()
    return user_choice

# ------------------ Determine Winner ------------------ #
def determine_round_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        return "user"
    else:
        return "computer"

# ------------------ Get Valid Number of Rounds ------------------ #
def get_total_rounds(user_name):
    while True:
        rounds_input = input(f"{user_name}, how many rounds do you want to play? ").strip()
        if rounds_input.isdigit():
            total_rounds = int(rounds_input)
            if total_rounds >= 1:
                return total_rounds
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Invalid input. Please enter a valid positive number.")

# ------------------ Main Game Function ------------------ #
def play_game():
    print("🐍💧🔫 Welcome to Snake, Water, Gun – Best of N Rounds!")
    user_name = input("Enter Your Name: ").strip().capitalize()
    total_rounds = get_total_rounds(user_name)

    user_score = 0
    computer_score = 0

    for round_num in range(1, total_rounds + 1):
        print(f"\n🔁 Round {round_num} of {total_rounds}")

        user_choice = get_valid_user_choice(user_name)
        computer_choice = generate_random_choice()

        print(f"\n🧍 ({user_name}) Your Choice: {user_choice.capitalize()}")
        print(f"💻 Computer's Choice: {computer_choice.capitalize()}")

        result = determine_round_winner(user_choice, computer_choice)

        if result == "tie":
            print(f"{user_name}, it's a tie!")
        elif result == "user":
            print(f"🎉 {user_name}, you win this round!")
            user_score += 1
        else:
            print(f"{user_name}, you lose this round.")
            computer_score += 1

    # ------------------ Final Score Summary ------------------ #
    print("\n📊 Final Score:")
    print(f"{user_name}: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print(f"🏆 Congratulations {user_name}, you won the game!")
    elif user_score < computer_score:
        print(f"😞 Sorry {user_name}, the computer won the game.")
    else:
        print("🤝 It's an overall tie!")

# ------------------ Main Loop ------------------ #
while True:
    play_game()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("👋 Thanks for playing! See you next time.")
        break
