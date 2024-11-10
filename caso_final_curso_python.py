import sympy

# Función para calcular el producto de los dígitos de un número
# Ejemplo: m(73) = 7 * 3 = 21
def m(n):
    return eval('*'.join(str(n)))

# Función para invertir un número, obteniendo su "número espejo"
# Ejemplo: r(73) = 37
def r(n):
    return int(str(n)[::-1])

# Generamos la lista de números primos hasta 1,000,000
# sympy.primerange(1, 1000000) devuelve un generador de primos en el rango [1, 1000000)
primos = list(sympy.primerange(1, 1000000))

# Iteramos sobre todos los números primos
for i, p in enumerate(primos):
    # Aseguramos que p sea un número de dos dígitos o más
    # La conjetura no aplica para números primos menores a 10
    if p >= 10:
        # Propiedad (b): El producto de los dígitos de p debe ser igual a su posición en la lista de primos (empezando desde 2)
        if m(p) == i + 1:
            # Propiedad (c): El número espejo de la posición (r(i+1)) debe coincidir con el número en la posición correspondiente
            # Ejemplo: Si p está en la posición 21, su número espejo (r(21) = 12) debe tener como primo el número en la posición 12
            if r(i + 1) - 1 < len(primos) and primos[r(i + 1) - 1] == r(p):
                # Imprimimos el número que cumple todas las condiciones de la Conjetura de Sheldon
                print(f"El número {p} cumple la Conjetura de Sheldon, en la posición {i + 1}")
                break  # Detenemos la búsqueda al encontrar el primer número que cumple la conjetura

