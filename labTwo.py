#Justin Farquharson
#09/13/2021
#COP 2500C
#Lab Two

#program to print all the odd numbers from 0 to n

n = int(input("Enter n:\n"))

#for i in range(1,n+1,2):
  #print(i)

#even numbers from 0 to n
#for i in range(0,n+1,2):
  #print(i)

#for i in range(1,n+1):
  #fact = fact * i

#print("Factorial of", n,"is =", fact)

fact = 1
i = 1
while i<=n:
  fact = fact * i
  i+=1

print("using while loop Factorial of", n, "is =", fact)
