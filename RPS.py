import random

def rock_paper_scissors():
    options = ["Rock", "Paper", "Scissors"]

    user_choice = input("\nChoose Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)

    if user_choice.lower() == computer_choice.lower():
        print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. It's a tie!")

    elif user_choice.lower() == 'rock':
        if computer_choice.lower() == 'scissors':
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. You win!")
        elif computer_choice.lower() == 'paper':
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. You lose!")

    elif user_choice.lower() == 'paper':
        if computer_choice.lower() == 'rock':
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. You win!")
        elif computer_choice.lower() == 'scissors':
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. You lose!")

    elif user_choice.lower() == 'scissors':
        if computer_choice.lower() == 'paper':
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. You win!")
        elif computer_choice.lower() == 'rock':
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}. You lose!")

    play_again = input("\nDo you want to play Rock, Paper, Scissors again? (Yes/No): ")
    if play_again.lower() == 'yes':
        rock_paper_scissors()
    elif play_again.lower() == 'no':
        print("\nThanks for playing! Have a great day!")
    else:
        print("Invalid choice. Please try again!")

play = input("\nDo you want to play Rock, Paper, Scissors? (Yes/No): ")

if play.lower() == 'yes':
    rock_paper_scissors()
elif play.lower() == 'no':
    print("Okay, have a good day!")
else:
    print("Invalid choice. Please try again!")
