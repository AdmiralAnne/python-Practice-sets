# lets use a library callled "random" 
from random import randint
# create a list of available choices
t = ['rock','paper','scizzor']

# let the computer choose a random option - r/p/s
computer=t[randint(0,len(t))]
# print(computer) # you can print the computer's choice and see the randness on every execution
# set Player to Flase - as in .. no choice picked yet
player=False
while player== False:
    # set player to True
    player=input("Rock, paper or Scizzor ?: ").lower()
    # compare choices with Computer and print appropriate output
    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "paper":
            print("You lose!",computer,"beats",player)
        else:
            print("You win!",player,"beats",computer)
    elif player == "paper":
        if computer == "scizzor":
            print("You lose!",computer,"beats",player)
        else:
            print("You win!",player,"beats",computer)
    elif player == "scizzor":
        if computer == "rock":
            print("You lose!",computer,"beats",player)
        else:
            print("You win!",player,"beats",computer)
    else:
        print("You may have entered a worng option~ Please try again! ")
    # we want the loop to continue but only if player chooses to do so
    print("Do you want to continue (y/n)?: ")
    choice=input().lower()
    # print(choice) # you can see that your choice is turned to lowercase
    if choice=='y':
        player=False
        computer=t[randint(0,len(t))]
    else:
        player=True
        print("Thank you for playing! ")
    