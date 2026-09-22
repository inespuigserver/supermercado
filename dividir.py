num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

resultado = 0

while num1 >= num2:
    num1 = num1 - num2
    resultado = resultado + 1

print("El resultado es:", resultado)