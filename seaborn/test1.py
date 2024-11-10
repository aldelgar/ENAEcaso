import sympy

# Función para calcular el producto de los dígitos de un número
def m(n):
    return eval('*'.join(str(n)))

# Función para invertir un número (número espejo)
def r(n):
    return int(str(n)[::-1])

# Generar lista de primos hasta 1,000,000
primos = list(sympy.primerange(1, 1000000))

# Función para verificar la Conjetura de Sheldon
def verificar_sheldon():
    for i, p in enumerate(primos):
        # Verificar la propiedad (a): El número debe ser primo
        if p < 10:  # Los números primos menores a 10 no cumplen las condiciones de la conjetura
            continue

        # Propiedad (b): m(p) debe ser igual a la posición del primo (empezando desde 2)
        if m(p) != i + 1:
            continue

        # Propiedad (c): El número espejo de la posición debe ser el número primo en esa posición
        espejo_pos = r(i + 1) - 1  # Ajustamos para que la posición esté basada en 0
        if espejo_pos < len(primos) and primos[espejo_pos] == r(p):
            print(f"El número {p} cumple la Conjetura de Sheldon, en la posición {i + 1}")
            return p  # Retorna el primer número que cumple la conjetura

    return None  # Si no encuentra ningún número que cumpla

# Llamar a la función para verificar
verificar_sheldon()
