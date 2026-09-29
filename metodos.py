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



# PARTE 2 DEL EJERCICIO
def calcular_horas_tareas(cantidades, horas_por_unidad):
    """Horas que tarda UN empleado en cada tarea (solo tareas con cantidad > 0)."""
    horas = []
    for c in cantidades:
        if c > 0:
            horas.append(c * horas_por_unidad)
    return horas


def quedan_pendientes(pendientes):
    for h in pendientes:
        if h > 0:
            return True
    return False


def simular_tiempo(horas_tareas, empleados_por_tarea, simultaneas, paso=0.25):
    """
    Funcion base para los 3 escenarios. Simula el paso del tiempo con un bucle.
    - empleados_por_tarea: cuantos empleados trabajan en cada tarea (acelera la tarea)
    - simultaneas: cuantas tareas se pueden hacer a la vez
    - paso: horas que avanza cada vuelta del bucle
    """
    if simultaneas < 1:
        raise ValueError("No hay empleados suficientes para formar un grupo")

    pendientes = horas_tareas[:]
    tiempo = 0

    while quedan_pendientes(pendientes):
        activas = 0
        for i in range(len(pendientes)):
            if pendientes[i] > 0 and activas < simultaneas:
                pendientes[i] = pendientes[i] - paso * empleados_por_tarea
                activas = activas + 1
        tiempo = tiempo + paso

    return tiempo


def tiempo_equitativo(horas_tareas, num_empleados):
    """Todos los empleados repartidos a partes iguales entre todas las tareas a la vez."""
    n = len(horas_tareas)
    return simular_tiempo(horas_tareas, num_empleados / n, n)


def tiempo_en_solitario(horas_tareas, num_empleados):
    """Cada empleado trabaja solo en una tarea (si hay 8 y 5 tareas, trabajan 5)."""
    simultaneas = min(num_empleados, len(horas_tareas))
    return simular_tiempo(horas_tareas, 1, simultaneas)


def tiempo_en_grupos(horas_tareas, num_empleados, tam_grupo):
    """Empleados en grupos (8 empleados de 2 en 2 = 4 tareas a la vez)."""
    simultaneas = division_entera(num_empleados, tam_grupo)
    return simular_tiempo(horas_tareas, tam_grupo, simultaneas)


def restar_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Los arrays deben tener la misma longitud")
    result = []
    for i in range(len(array1)):
        result.append(array1[i] - array2[i])
    return result


def sumar_lista(lista):
    total = 0
    for x in lista:
        total = total + x
    return total