#Justin Farquharson
#COP 2500C
#8/26/2021
#Review of Day One

print("Welcome to Day 2!", end="")

print("I\nNeed\nLess\nHomework")

print("\n")



#Variables and Input

idcardGrade = 12

print("Id Card:", idcardGrade)

justinGPA = 3.75

print("GPA:", justinGPA, "- not bad :)")




#Target List

print("\n")

pens = int (input("How many pens would you like to buy?\n"))
paper = float (input("How many pieces of paper would you like?\n"))

penPrice = 0.10
paperPrice = 0.25

totalPensPrice = pens * penPrice

print("Total Price of Pens: $", totalPensPrice, sep="")

totalPaperPrice = paper * paperPrice

print("Total Price of Paper: $", totalPaperPrice, sep="")

print("Total Price: $", totalPensPrice + totalPaperPrice, sep="")
