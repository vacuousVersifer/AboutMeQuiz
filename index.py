print("Quiz time :o)")

print("Would you like to play?")
ans = input("(yes / no): ").lower()

if ans == "yes":
    print("Very good.")

    score = 0
    totalQuestions = 4

    print("1. What galaxy was I born in?")
    answerOne = input().lower()
    if answerOne == "the milky way":
        score += 1
        print("Correct!!")
    else: 
        print("Nope :,(")

    print("2. What yarn craft do I partake in?")
    answerOne = input().lower()
    if answerOne == "crochet":
        score += 1
        print("Correct!!")
    else: 
        print("Nope :,(")

    print("3. How many kids do I have?")
    answerTwo = input().lower()
    if answerTwo == "0":
        score += 1
        print("Correct!!")
    else: 
        print("Nope :,(")

    print("4. What is my favorite pizza topping?")
    answerTwo = input().lower()
    if answerTwo == "pepperoni":
        score += 1
        print("Correct!!")
    else: 
        print("Nope :,(")

    print("The quiz is done.")
    print("Your score is: ", score)

    finalScore = (score / totalQuestions) * 100
    print("That's ", finalScore, "%")

elif ans == "no":
    print("Your detriment, I suppose")
else:
    print("Uh, what did you just say?")