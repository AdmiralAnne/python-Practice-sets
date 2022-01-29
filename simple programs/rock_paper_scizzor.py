import random


def play():
    user = input(
        "\nwhats your choice\n'R' for Rock, 'P' for paper, 'S' for scizzors: "
    ).lower()
    computer = random.choice(["r", "p", "s"])  # computer randomly chooses from the list
    print(f'\nyou : {user}') 
    print(f'Computer : {computer} \n') 
    if user == computer:
        return "It's a tie\n"

    if is_win(user, computer):
        return "You Won the game!\n"
        value=True

    return "You Lost the game\n"

def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True

def play_again():
    choice=input("Do you want to play again? (YES/NO)\n").lower()
    if choice=="yes":
        return True
    elif choice=="no":
        print("Thank You For playing With us!!!")
    else:
        play_again()




print(play())  # since we are not directly not passsing any argument to the function

while play_again():
    print(play())
