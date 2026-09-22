def division_entera(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        resultado = 0

        while a >= b:
            a = a - b
            resultado = resultado + 1

        return resultado


def modulo(a, b):
    division = a // b
    return a - (division * b)


def potencia(x, y):
    resultado = 1

    for i in range(y):
        resultado = resultado * x

    return resultado


def ordenar_array(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def sum_arrays(array1, array2):
    if len(array1) != len(array2):
        return None

    result = []

    for i in range(len(array1)):
        result.append(array1[i] + array2[i])

    return result


def matrix_sum(matrix_a, matrix_b):

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    result = []

    for i in range(len(matrix_a)):
        fila = []

        for j in range(len(matrix_a[0])):
            fila.append(matrix_a[i][j] + matrix_b[i][j])

        result.append(fila)

    return result