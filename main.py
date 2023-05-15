import random


def get_choices():
  options = ["rock", "paper", "scissors"]
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  return choices



def check_win(player, computer):
  print(f"You chose {player} , and computer chose {computer}")
  
  if player == computer:
    return "It's a tie!"

  
  elif player == "rock":
    
    if computer == "scissors":
      return ("Rock smashes scissors!! You win!!")

    else :
      return ("Paper covers rock. Sorry, you lost :((")

  
  elif player == "paper":
    
    if computer == "rock":
      return ("Paper covers rock!! YOu win!!")

    else :
      return ("Scissors cut paper. Sorry, you lost :((")

  elif player == "scissors":

    if computer == "paper":
      return ("Scissor cut paper!! You win!!")

    else :
      return ("Rock smashes scissors. Sorry, you lost :((")


final_choices = get_choices()

player_choice = final_choices["player"]
computer_choice = final_choices["computer"]

result = check_win(player_choice, computer_choice)

print(result)