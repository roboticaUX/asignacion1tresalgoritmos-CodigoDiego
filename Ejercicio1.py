from ast import If
n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese un segundo numero: "))
if n2==n1:
    n2=float(input("Los numeros no se pueden repetir, ingrese otro: "))
n3=float(input("Ingrese un tercer número: "))
if n3==n2 or n3==n1:
    n3=float(input("Los números no se pueden repetir, ingrese otro: "))
nums=[n1,n2,n3]
nums.sort(reverse=True)
print("Sus números son: ",nums)