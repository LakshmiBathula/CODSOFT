import random

def rock_paper_scissor():
    user_s = 0
    computer_s= 0

    while True:
        print("\nRock, Paper, Scissors Game")
        
        user_c= input("Choose rock, paper, or scissors: ").lower()
        computer_c = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYou chose: {user_c}")
        print(f"Computer chose: {computer_c}")

        if user_c == computer_c:
            result = 'Tie'
        elif (user_c == 'rock' and computer_c == 'scissors') or \
             (user_c== 'scissors' and computer_c== 'paper') or \
             (user_c == 'paper' and computer_c== 'rock'):
            result = 'You win!'
            user_s += 1
        else:
            result = 'Computer wins!'
            computer_s += 1

        print(result)
        print(f"\nScore - You: {user_s}, Computer: {computer_s}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    rock_paper_scissor()
