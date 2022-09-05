n = int(input("Ingrese el número a calcular su factorial: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i     
print ("El factorial de ",n,"es: ",end="")
print (fact)