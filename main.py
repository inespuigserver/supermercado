from time import time

import productos
import super


<<<<<<< HEAD
# Numero de clientes que entraran al supermercado
numero_clientes = 20

# Dinero total generado por las compras
ingresos_totales = 0


print("================================")
print("     SIMULACION SUPERMERCADO")
print("================================")


# Simulamos las compras de los clientes
for i in range(numero_clientes):

    print("\nCLIENTE", i + 1)

    coste_compra = super.compra_random(
        productos.productos,
        productos.precios,
        productos.stock_supermercado
    )

    ingresos_totales = ingresos_totales + coste_compra


# Mostramos el resultado final de la simulacion
print("\n================================")
print("        FIN DE LA SIMULACION")
print("================================")

print("\nClientes atendidos:", numero_clientes)
print("Ingresos totales:", round(ingresos_totales, 2), "€")


# Mostramos el stock que queda en el supermercado
print("\nSTOCK FINAL DEL SUPERMERCADO")
print("--------------------------------")

for i in range(len(productos.productos)):
    print(
        productos.productos[i],
        "-",
        productos.stock_supermercado[i],
        "unidades"
    )