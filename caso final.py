import sympy

# Función para calcular el producto de los dígitos
def m(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

# Función para invertir los dígitos
def r(n):
    return int(str(n)[::-1])

# Generar lista de números primos hasta 1,000,000
primes = list(sympy.primerange(1, 1000000))

# Almacenar números de Sheldon
sheldon_numbers = []

# Recorrer los números primos
for index, prime in enumerate(primes):
    position = index + 1  # Las posiciones inician en 1
    if m(prime) == position:
        # Calcular el número espejo
        mirrored_prime = r(prime)
        # Obtener la posición del número espejo
        if mirrored_prime in primes:
            mirrored_position = primes.index(mirrored_prime) + 1  # Posición del número espejo
            # Verificar la propiedad del espejo
            if r(position) == mirrored_prime:
                sheldon_numbers.append(prime)

# Resultado
sheldon_numbers
