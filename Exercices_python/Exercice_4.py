#Exercice_4

n = int(input("Enter a number please: "))
res = 0
i = 1
while i <= n:
    res += i 
    i+=1
    
    
print("The sum of numbers lowers than {} is: {}".format(n, res))