#Python quiz game

questions=("What is the capital city of Germany?:",
           "Which country won the FIFA World Cup in 2018?:",
           "What planet is known as the Red Planet?:",
           "Who wrote Romeo and Juliet?:",
           "Which language has the most native speakers worldwide?:")

options=(("A.Switzerland","B.London ","C.France ","D.Berlin "),
         ("A.England","B.France ","C.South Korea ","D.USA "),
         ("A.Pluto ","B.Jupiter ","C.Mars ","D.Earth"),
         ("A.Winston Churchill ","B.Oscar Wilde ","C.William Shakespeare ","D.Wright Brothers "),
         ("A.Mandarin ","B.Tamil ","C.English ","D.German "))

answers=("D", "B", "C", "C","A")
guesses= []
score = 0
question_num=0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score +=1
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1


print("---------------------------")
print("          RESULT           ")
print("---------------------------")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")