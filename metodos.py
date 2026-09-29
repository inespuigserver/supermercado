import time
import super
import productos

def division_entera(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    resultado = 0
    while a >= b:
        a = a - b
        resultado = resultado + 1
    return resultado


def modulo(a, b):
    return a - b * division_entera(a, b)


def ordenar_array(arr):
    arr = arr[:]  
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def potencia(x, y):
    resultado = 1

    for i in range(y):
        resultado = resultado * x

    return resultado


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

def step():
    super.compra_random(
        productos.productos,
        productos.precios,
        productos.stock_supermercado
    )
    time.sleep(3)


def buscar_indice(nombre, lista_nombres):
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre:
            return i
    return -1


def coste_total(nombres, cantidades):
    """Recibe nombres de productos y cantidades, devuelve el coste total en €."""
    if len(nombres) != len(cantidades):
        raise ValueError("nombres y cantidades deben tener la misma longitud")

    total = 0
    for i in range(len(nombres)):
        pos = buscar_indice(nombres[i], productos.productos)
        if pos == -1:
            raise ValueError("El producto no existe: " + nombres[i])
        total = total + productos.precios[pos] * cantidades[i]

    return total


def repartir_en_cajas(unidades, unidades_por_caja):
    """Devuelve (cajas completas, unidades sueltas)."""
    return division_entera(unidades, unidades_por_caja), modulo(unidades, unidades_por_caja)