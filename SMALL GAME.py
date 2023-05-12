print("Welcome to the Jesse Quiz!")

answer = input("Are you ready to play the Quiz? [yes/no]: ")

score = 0
total_questions = 4


if answer.lower() == "yes":
    answer=input("1. Is  Jesse Happy? ")
    if answer.lower() == "yes":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    answer=input("1. What is his favourtie football team? ")


    if answer.lower()== "Arsenal":
        score +=2
        print("correct")
    else:
        print("incorrect")
    
print("Thank you for playing, you got", score, "questions correct.")
