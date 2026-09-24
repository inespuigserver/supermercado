# Nombres de los productos
#pycache
productos = [
    "Manzana",
    "Platano",
    "Pasta",
    "Arroz",
    "Leche",
    "Huevos",
    "Pan",
    "Pollo",
    "Carne picada",
    "Yogur",
    "Queso",
    "Jamon cocido",
    "Atun en lata",
    "Tomate",
    "Patatas",
    "Cebolla",
    "Aceite de oliva",
    "Sal",
    "Azucar",
    "Cafe",
    "Agua mineral",
    "Coca-Cola",
    "Zumo de naranja",
    "Cerveza",
    "Detergente",
    "Suavizante",
    "Jabon de manos",
    "Papel higienico",
    "Lejia",
    "Limpiacristales"
]


# Precio de cada producto

precios = [
    0.45,   # Manzana
    0.35,   # Platano
    1.20,   # Pasta
    1.40,   # Arroz
    1.10,   # Leche
    2.50,   # Huevos
    0.90,   # Pan
    5.50,   # Pollo
    4.80,   # Carne picada
    1.00,   # Yogur
    3.20,   # Queso
    2.80,   # Jamon cocido
    1.60,   # Atun en lata
    0.60,   # Tomate
    2.00,   # Patatas
    0.50,   # Cebolla
    6.50,   # Aceite de oliva
    0.80,   # Sal
    1.30,   # Azucar
    3.50,   # Cafe
    0.70,   # Agua mineral
    1.50,   # Coca-Cola
    1.80,   # Zumo de naranja
    1.20,   # Cerveza
    4.50,   # Detergente
    3.20,   # Suavizante
    1.80,   # Jabon de manos
    4.00,   # Papel higienico
    2.00,   # Lejia
    2.80    # Limpiacristales
]


# Stock inicial disponible en las estanterias del supermercado

stock_supermercado = [
    30,     # Manzana
    30,     # Platano
    20,     # Pasta
    20,     # Arroz
    35,     # Leche
    25,     # Huevos
    30,     # Pan
    15,     # Pollo
    15,     # Carne picada
    30,     # Yogur
    15,     # Queso
    15,     # Jamon cocido
    20,     # Atun en lata
    30,     # Tomate
    25,     # Patatas
    25,     # Cebolla
    12,     # Aceite de oliva
    15,     # Sal
    15,     # Azucar
    15,     # Cafe
    40,     # Agua mineral
    30,     # Coca-Cola
    20,     # Zumo de naranja
    25,     # Cerveza
    10,     # Detergente
    10,     # Suavizante
    12,     # Jabon de manos
    15,     # Papel higienico
    10,     # Lejia
    10      # Limpiacristales
]


# Stock inicial disponible en el almacen

stock_almacen = [
    120,    # Manzana
    120,    # Platano
    100,    # Pasta
    100,    # Arroz
    150,    # Leche
    100,    # Huevos
    120,    # Pan
    80,     # Pollo
    80,     # Carne picada
    120,    # Yogur
    80,     # Queso
    80,     # Jamon cocido
    100,    # Atun en lata
    120,    # Tomate
    120,    # Patatas
    100,    # Cebolla
    60,     # Aceite de oliva
    80,     # Sal
    80,     # Azucar
    80,     # Cafe
    150,    # Agua mineral
    130,    # Coca-Cola
    100,    # Zumo de naranja
    120,    # Cerveza
    60,     # Detergente
    60,     # Suavizante
    70,     # Jabon de manos
    80,     # Papel higienico
    60,     # Lejia
    60      # Limpiacristales
]


# Cuando el stock del supermercado llegue a estos valores habrá que solicitar productos al almacen.

stock_minimo_supermercado = [
    8,      # Manzana
    8,      # Platano
    5,      # Pasta
    5,      # Arroz
    8,      # Leche
    6,      # Huevos
    8,      # Pan
    4,      # Pollo
    4,      # Carne picada
    8,      # Yogur
    4,      # Queso
    4,      # Jamon cocido
    5,      # Atun en lata
    8,      # Tomate
    6,      # Patatas
    6,      # Cebolla
    3,      # Aceite de oliva
    4,      # Sal
    4,      # Azucar
    4,      # Cafe
    10,     # Agua mineral
    8,      # Coca-Cola
    5,      # Zumo de naranja
    6,      # Cerveza
    3,      # Detergente
    3,      # Suavizante
    3,      # Jabon de manos
    4,      # Papel higienico
    3,      # Lejia
    3       # Limpiacristales
]


# Cuando el almacen llegue a estos valores habrá que pedir nuevas unidades a la fabrica.

stock_minimo_almacen = [
    30,     # Manzana
    30,     # Platano
    25,     # Pasta
    25,     # Arroz
    35,     # Leche
    25,     # Huevos
    30,     # Pan
    20,     # Pollo
    20,     # Carne picada
    30,     # Yogur
    20,     # Queso
    20,     # Jamon cocido
    25,     # Atun en lata
    30,     # Tomate
    30,     # Patatas
    25,     # Cebolla
    15,     # Aceite de oliva
    20,     # Sal
    20,     # Azucar
    20,     # Cafe
    40,     # Agua mineral
    30,     # Coca-Cola
    25,     # Zumo de naranja
    30,     # Cerveza
    15,     # Detergente
    15,     # Suavizante
    15,     # Jabon de manos
    20,     # Papel higienico
    15,     # Lejia
    15      # Limpiacristales
]

# Stock disponible en la fábrica
stock_fabrica = [
    500,  # Manzana
    500,  # Platano
    400,  # Pasta
    400,  # Arroz
    500,  # Leche
    400,  # Huevos
    450,  # Pan
    300,  # Pollo
    300,  # Carne picada
    450,  # Yogur
    300,  # Queso
    300,  # Jamon cocido
    350,  # Atun en lata
    450,  # Tomate
    450,  # Patatas
    400,  # Cebolla
    250,  # Aceite de oliva
    300,  # Sal
    300,  # Azucar
    300,  # Cafe
    600,  # Agua mineral
    500,  # Coca-Cola
    400,  # Zumo de naranja
    450,  # Cerveza
    250,  # Detergente
    250,  # Suavizante
    280,  # Jabon de manos
    300,  # Papel higienico
    250,  # Lejia
    250   # Limpiacristales
]
