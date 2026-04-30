import random

def guessing_game():
    """A fun number guessing game"""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    play_again = True
    
    while play_again:
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0
        guessed = False
        
        print(f"\nI'm thinking of a number between 1 and 100.")
        print("Can you guess what it is?\n")
        
        while not guessed:
            try:
                # Get user input
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                # Validate input range
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100!")
                    continue
                
                # Check the guess
                if guess == secret_number:
                    guessed = True
                    print(f"\n🎉 Correct! You guessed {secret_number} in {attempts} attempt(s)!")
                    
                    # Provide feedback on performance
                    if attempts == 1:
                        print("Amazing! You got it on the first try!")
                    elif attempts <= 5:
                        print("Excellent! That was very quick!")
                    elif attempts <= 10:
                        print("Good job! You figured it out.")
                    else:
                        print("You got it! Keep practicing to improve!")
                
                elif guess < secret_number:
                    print(f"❌ Too low! Try a higher number. (Attempt {attempts})")
                
                else:  # guess > secret_number
                    print(f"❌ Too high! Try a lower number. (Attempt {attempts})")
            
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        # Ask if user wants to play again
        while True:
            play_choice = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_choice in ['yes', 'y']:
                play_again = True
                break
            elif play_choice in ['no', 'n']:
                play_again = False
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("Please enter 'yes' or 'no'.")
    
    print("=" * 50)

if __name__ == "__main__":
    guessing_game()