def dividir (A, B):
    if B == 0:
        return "Error: No se puede dividir entre cero"
    else:
        Resultado = 0
        while A >= B:
            A = A - B
            Resultado = Resultado + 1

    return Resultado
print(dividir(14, 2))


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