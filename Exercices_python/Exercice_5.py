#Exercice_5

n = int(input("Please enter a number:"))

fact = 1
i = 1
if n < 2:
    pass
else:
    while i <= n:
        fact = fact * i
        i+=1
    

print("The factorial of {} is {}: ".format(n, fact))