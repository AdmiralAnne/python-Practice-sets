# -------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num - 1]:  # get zero as the initial val
            print(i)
        guess = input("Enter (A , B, C, D):").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


# -------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------")
    print("RESULTS")
    print("----------------------------------------")
    print("ANSWERS: ", end="")
    for (
        i
    ) in questions:  # our dictionary. use get() to get the values of corresponding key
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ", end="")
    for i in guesses:  # guesses is the list with all our Guesses
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    # score divided by total times 100 to get the percentage
    print("Your score is: " + str(score) + "%")


# -------------------
def play_again():

    response = input("Do you want to play again? (Yes or No) ").upper()

    if response == "YES":
        return True
    else:
        return False


# -------------------


questions = {
    "Who created Google?": "C",
    "Is the Earth Round?": "A",
    "Did Bill Gates work for Apple?": "D",
    "Who is Elon Musk?": "C",
}

options = [
    ["A. Larry Page", "B. Sergey Brin", "C.BOTH A and B", "D. Britney Spears"],
    ["A. Of course!", "B. Its Flat! facts ", "C. whats's Earth? ", "D. Ask Gandalf"],
    [
        "A. Yes, He founded it",
        "B. No, he worked for Google",
        "C. He isn't even a real person",
        "D. Isnt he related to microsoft",
    ],
    ["A. An Astronaut", "B. Famous Footballer", "C.X Æ A-12's Daddy", "D. A greek God"],
]


new_game()

while play_again():  # if TRUE, then start a new game else Print Bye~
    new_game()

print("BYEE Thanks for playing")
