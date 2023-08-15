import random

user_wins = 0
computer_wins = 0
option = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q for quit: ").lower()
    if user_input == "q":
       print("your score", user_wins)
       print("computer score",computer_wins)
       if computer_wins>user_wins:
           print("YOU LOST :(, Try next time!")
           quit()
       else:
           print("CONGRATULATION :) YOU WON!")
           print("Goodbye")
           quit()
    if user_input not in option:
        continue
    random_number = random.randint(0,2)
    computer_pick = option[random_number]
    print("computer picked ",computer_pick," .")

    if user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins +=1
    elif user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins +=1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins +=1
    elif user_input == computer_pick:
        print("same same")
    else:
        print("you lost")
        computer_wins +=1
      
