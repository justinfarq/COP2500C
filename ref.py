#Reference

a=int(input("Enter whole number: \n"))
print(a)

b=float(input("Enter decimal: \n"))
print(b)

sum= a+b

mul= a*b

div= a/b

x=13.33333*4.567556
less=format(x,".2f")

#even numbers from 0 to n
for i in range(0,n+1,2):
    print(i)

#program to print all the odd numbers from 0 to n
for i in range(1,n+1,2):
    print(i)

#Print Remainder after 5 is divided by 2
print(5%2)

#Prints 5/2 without remainder
print(5//2)

#With remainder
print(5/2)

while (option != 3):
    if (option == 1):
        number = 7
        guess = int(input("Guess my lucky number\n"))
        if (number == guess):
            print("You got it right!")
        else:
            print("You lose.")
