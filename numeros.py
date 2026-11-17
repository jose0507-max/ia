num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

aux = 0

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

if num1 > num3:
    aux = num1
    num1 = num3
    num3 = aux

if num2 > num3:
    aux = num2
    num2 = num3
    num3 = aux

print("Numeros ordenados de menor a mayor:")
print(num1, num2, num3)