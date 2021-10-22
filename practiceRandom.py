import random

hiddenNumber = random.randint(1,100)

#Testing purposes
print(hiddenNumber)

guess = 0

score = 0
maxGuesses = 10

play = True

while(play == True):

    while (guess != hiddenNumber and score < maxGuesses):

        guess = int(input("What is your guess?\n"))
    
        if (guess < hiddenNumber):
            print("You guess too low.")
            score = score + 1
        elif(guess > hiddenNumber):
            print("You guess too high.")
            score = score + 1
        else:
            print("You got it correct!")

    if (score == maxGuesses):
        print("You lose, you guessed too many times")
    else:
        print("Your score was", score)

    again = input("Would you like to play again?\n")
    if (again == "no"):
        play = False
    else:
        score = 0
        guess = 0
        hiddenNumber = random.randint(1,100)
        print(hiddenNumber)

print("You won", wins, "times and lost", loss, "times")
