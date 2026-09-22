num1 = 20
num2 = 5

resultado = 0

while num1 >= num2:
    num1 = num1 - num2
    resultado = resultado + 1

print("El resultado es:", resultado)


def modulo(a, b):
    division_entera = a // b
    return a - (division_entera * b)
print(modulo(10, 3))

def ordenar_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr