#Justin Farquharson
#09/07/2021
#COP 2500C
#Day Four

grade = float(input("What grade do you have in this class?\n"))

if (grade >= 90):
    print("A")
elif (grade >= 80):
    print("B")
elif (grade >= 70):
    print("C")
else:
    print("F")

print("All done.")


number = 5

while (number < 10):
    print(number)
    number = number+2

print("Menu\n")
print("1. Play a game\n")
print("2. Find my grade\n")
print("3. Quit\n")

option = int(input("Input the number choice\n"))

while (option != 3):
    if (option == 1):
        number = 7
        guess = int(input("Guess my lucky number\n"))
        if (number == guess):
            print("You got it right!")
        else:
            print("You lose.")
    elif (option == 2):
            grade = float(input("What grade do you have in this class?\n"))
            if (grade >= 90):
                print("A")
            elif (grade >= 80):
                print("B")
            elif (grade >= 70):
                print("C")
            else:
                print("F")
    else:
        print("Invalid choice")

        print("Menu\n")
        print("1. Play a game\n")
        print("2. Find my grade\n")
        print("3. Quit\n")

        option = int(input("Input the number choice\n"))
        
