def division_entera(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        resultado = 0
        while a >= b:
            a = a - b
            resultado = resultado + 1
        return resultado
    
resultado = division_entera(10, 3)
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

def sum_arrays(array1, array2):
    if len(array1) != len(array2):
        return None

    result = []

    for i in range(len(array1)):
        result.append(array1[i] + array2[i])

    return result
