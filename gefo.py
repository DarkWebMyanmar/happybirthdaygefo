def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print(key)

        for i in choices[question_num-1]:
            print(i)
        guess=input("Enter A, B, C, or D : ").upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        print("------------------------------")
        question_num+=1
    display_score(correct_guesses,guesses)
#-------------------------
def check_answer(answer,guess):
    if answer==guess:
        print("Correct!")
        return 1
    else:
        print("Wrong Answer!")
        return 0
#-------------------------
def display_score(correct_guesses,guesses):

    print("Results")
    print("-----------------------------")

    print("Correct Answers:",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Your choices:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score= int((correct_guesses/len(questions))*100)
    print("Your score is "+str(score)+"%.")
#-------------------------
def play_again():
    response=input("Do you want to play again?(yes or no): ").upper()
    if response=="YES":
        return True
    else:
        return False
#-------------------------

questions={
    "Who created Python?: ":"C",
    "Which dimension is time?: ":"C",
    "What is my date of birth?: ":"B",
    "Is the Earth round?: ":"A",
    "Which metal is the strongest in the world?: ":"D"
}

choices=[["A. Elon Musk","B. Warren Buffett","C. Guido van Rossum","D. Bernard Arnault"],
         ["A. 2D","B. 1D","C. 4D","D. 3D"],
         ["A. 25/5/2005","B. 26/5/2005","C. 27/5/2005","D. 28/5/2005"],
         ["A. Yes,it is.","B. Perhaps.","C. No, the earth is flat.","D. I don't know."],
         ["A. Titanium","B. Diamond","C. Silicon","D. Tungsten"]]

new_game()
while play_again():
    new_game()
print("Alright!\nPlease, don't take it too serious if some of your answers were wrong.\nAnyway,Thanks for your time:)\nHave a nice day!")
