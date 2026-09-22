x = int(input("Introduce la base: "))
y = int(input("Introduce el exponente: "))

resultado = 1  

for i in range(y):  
    resultado = resultado * x

print(f"{x} elevado a {y} es: {resultado}")
