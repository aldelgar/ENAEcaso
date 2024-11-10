import numpy as np
def esprimo(n):
    for i in range(2, int(np.sqrt(n)) + 1):
        if np.mod(n, i) == 0:
            return False
    return True
contador = 0
numero = 1
primo73 = {}
while contador < 73:
    numero += 1
    if esprimo(numero):
        contador += 1
        primo73 = numero
print(primo73)
