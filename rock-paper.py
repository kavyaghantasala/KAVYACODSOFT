import random

def get_user_choice():
    """Prompt user for rock, paper, or scissors and validate input."""
    valid_choices = {
        'r': 'rock', 'rock': 'rock',
        'p': 'paper', 'paper': 'paper',
        's': 'scissors', 'scissors': 'scissors'
    }
    while True:
        choice = input("Enter your choice (rock/paper/scissors or r/p/s): ").lower().strip()
        if choice in valid_choices:
            return valid_choices[choice]
        print("Error: Please enter rock, paper, scissors, or r, p, s.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie', None  # No score change for tie
    
    winning_combinations = {
        ('rock', 'scissors'): 'user',
        ('scissors', 'paper'): 'user',
        ('paper', 'rock'): 'user'
    }
    
    if (user_choice, computer_choice) in winning_combinations:
        return 'user', 1  # User wins, +1 to user score
    return 'computer', 1  # Computer wins, +1 to computer score

def display_result(user_choice, computer_choice, result, user_score, computer_score):
    """Display the choices, result, and current scores."""
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins!")
    
    print(f"Scores - You: {user_score}, Computer: {computer_score}\n")

def play_again():
    """Ask if the user wants to play another round."""
    while True:
        response = input("Do you want to play again? (yes/no or y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False
        print("Error: Please enter yes, no, y, or n.")

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    print("Welcome to Rock-Paper-Scissors!")
    print("------------------------------")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("Enter your choice as rock, paper, scissors, or r, p, s.\n")
    
    user_score = 0
    computer_score = 0
    
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Determine winner and update scores
        result, score_point = determine_winner(user_choice, computer_choice)
        if result == 'user':
            user_score += score_point
        elif result == 'computer':
            computer_score += score_point
        
        # Display results
        display_result(user_choice, computer_choice, result, user_score, computer_score)
        
        # Ask to play again
        if not play_again():
            print(f"\nFinal Scores - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()