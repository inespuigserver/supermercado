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
