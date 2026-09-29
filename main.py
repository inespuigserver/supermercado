import productos
import super
import metodos

# Numero de clientes que entraran al supermercado
numero_clientes = 100

# Dinero total generado durante la simulacion
ingresos_totales = 0

# Contadores para ver cuantas reposiciones se realizan
reposiciones_supermercado = 0
pedidos_fabrica = 0


# Guardamos el stock inicial para saber hasta cuanto hay que reponer
stock_objetivo_supermercado = productos.stock_supermercado.copy()
stock_objetivo_almacen = productos.stock_almacen.copy()


print("========================================")
print("        SIMULACION SUPERMERCADO")
print("========================================")


# SIMULACION DE CLIENTES
for cliente in range(numero_clientes):

    print("\n========================================")
    print("CLIENTE", cliente + 1)
    print("========================================")

    # El cliente realiza una compra aleatoria
    coste_compra = super.compra_random(
        productos.productos,
        productos.precios,
        productos.stock_supermercado
    )

    ingresos_totales = ingresos_totales + coste_compra


    # COMPROBAR STOCK DEL SUPERMERCADO
    for i in range(len(productos.productos)):

        if productos.stock_supermercado[i] <= productos.stock_minimo_supermercado[i]:

            print(
                "\nSTOCK BAJO EN SUPERMERCADO:",
                productos.productos[i]
            )

            # Calculamos cuantas unidades hacen falta para
            # volver al stock inicial
            cantidad_necesaria = (
                stock_objetivo_supermercado[i]
                - productos.stock_supermercado[i]
            )


            # COMPROBAR SI EL ALMACEN TIENE SUFICIENTE STOCK
            if productos.stock_almacen[i] < cantidad_necesaria:

                print(
                    "El almacen no tiene suficiente stock de",
                    productos.productos[i]
                )

                print("Solicitando productos a la fabrica...")


                # La fabrica tiene stock infinito
                cantidad_fabrica = (
                    stock_objetivo_almacen[i]
                    - productos.stock_almacen[i]
                )

                productos.stock_almacen[i] = (
                    productos.stock_almacen[i]
                    + cantidad_fabrica
                )

                pedidos_fabrica = pedidos_fabrica + 1


                print(
                    "FABRICA -> ALMACEN:",
                    cantidad_fabrica,
                    "unidades de",
                    productos.productos[i]
                )


            # REPONER EL SUPERMERCADO DESDE EL ALMACEN

            productos.stock_almacen[i] = (
                productos.stock_almacen[i]
                - cantidad_necesaria
            )

            productos.stock_supermercado[i] = (
                productos.stock_supermercado[i]
                + cantidad_necesaria
            )

            reposiciones_supermercado = (
                reposiciones_supermercado + 1
            )


            print(
                "ALMACEN -> SUPERMERCADO:",
                cantidad_necesaria,
                "unidades de",
                productos.productos[i]
            )

            print(
                "Nuevo stock supermercado:",
                productos.stock_supermercado[i]
            )

            print(
                "Nuevo stock almacen:",
                productos.stock_almacen[i]
            )


            # COMPROBAR STOCK DEL ALMACEN

            if productos.stock_almacen[i] <= productos.stock_minimo_almacen[i]:

                print(
                    "Stock bajo en almacen de",
                    productos.productos[i]
                )

                print("Solicitando productos a la fabrica...")


                # Cantidad necesaria para devolver el almacen
                # a su stock inicial
                cantidad_fabrica = (
                    stock_objetivo_almacen[i]
                    - productos.stock_almacen[i]
                )

                productos.stock_almacen[i] = (
                    productos.stock_almacen[i]
                    + cantidad_fabrica
                )

                pedidos_fabrica = pedidos_fabrica + 1


                print(
                    "FABRICA -> ALMACEN:",
                    cantidad_fabrica,
                    "unidades de",
                    productos.productos[i]
                )

                print(
                    "Nuevo stock almacen:",
                    productos.stock_almacen[i]
                )


# FIN DE LA SIMULACION

print("\n\n========================================")
print("          FIN DE LA SIMULACION")
print("========================================")

print("Clientes atendidos:", numero_clientes)

print(
    "Ingresos totales:",
    round(ingresos_totales, 2),
    "€"
)

print(
    "Reposiciones del supermercado:",
    reposiciones_supermercado
)

print(
    "Pedidos realizados a la fabrica:",
    pedidos_fabrica
)


# STOCK FINAL DEL SUPERMERCADO

print("\n========================================")
print("      STOCK FINAL SUPERMERCADO")
print("========================================")

for i in range(len(productos.productos)):

    print(
        productos.productos[i],
        "-",
        productos.stock_supermercado[i],
        "unidades"
    )


# STOCK FINAL DEL ALMACEN

print("\n========================================")
print("         STOCK FINAL ALMACEN")
print("========================================")

for i in range(len(productos.productos)):

    print(
        productos.productos[i],
        "-",
        productos.stock_almacen[i],
        "unidades"
    )

# USO DE metodos.py

# Stock total por producto (supermercado + almacen)
stock_total = metodos.sum_arrays(productos.stock_supermercado, productos.stock_almacen)

print("\n========================================")
print("   STOCK TOTAL (SUPERMERCADO + ALMACEN)")
print("========================================")

for i in range(len(productos.productos)):
    print(productos.productos[i], "-", stock_total[i], "unidades")

# Stock total ordenado de menor a mayor
stock_ordenado = metodos.ordenar_array(stock_total)
print("\nStock total ordenado:", stock_ordenado)
print("Menor stock:", stock_ordenado[0], "| Mayor stock:", stock_ordenado[-1])

# Stock del almacen en cajas de 12
UNIDADES_POR_CAJA = 12

print("\n========================================")
print("      ALMACEN EN CAJAS DE", UNIDADES_POR_CAJA)
print("========================================")

for i in range(len(productos.productos)):
    cajas, sueltas = metodos.repartir_en_cajas(productos.stock_almacen[i], UNIDADES_POR_CAJA)
    print(productos.productos[i], "-", cajas, "cajas y", sueltas, "sueltas")

# Coste de un pedido (funcion nueva del ejercicio)
nombres_pedido = ["Leche", "Pan", "Cafe"]
cantidades_pedido = [50, 30, 20]

print("\nCoste del pedido:", round(metodos.coste_total(nombres_pedido, cantidades_pedido), 2), "€")




# PARTE II: TIEMPO DE REPOSICION SEGUN EMPLEADOS

HORAS_POR_UNIDAD = 0.1  # un empleado tarda 6 minutos por unidad repuesta

# Unidades que faltan en cada estanteria para volver al stock inicial
faltan = metodos.restar_arrays(stock_objetivo_supermercado, productos.stock_supermercado)
horas_tareas = metodos.calcular_horas_tareas(faltan, HORAS_POR_UNIDAD)

print("\n========================================")
print("   PARTE II: TIEMPO DE REPOSICION")
print("========================================")
print("Tareas de reposicion:", len(horas_tareas))
print("Horas totales para un solo empleado:", round(metodos.sumar_lista(horas_tareas), 2))

for empleados in [4, 8, 12]:
    print("\n--- Con", empleados, "empleados ---")
    print("Equitativo:", round(metodos.tiempo_equitativo(horas_tareas, empleados), 2), "horas")
    print("Cada uno solo:", round(metodos.tiempo_en_solitario(horas_tareas, empleados), 2), "horas")
    print("En grupos de 2:", round(metodos.tiempo_en_grupos(horas_tareas, empleados, 2), 2), "horas")