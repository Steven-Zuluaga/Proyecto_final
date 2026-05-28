# Factorial
def factorial(n):
    if n < 0:
        print(' Error: El factorial no existe para negativos.')
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


# Raiz Cuadrada
def raiz_cuadrada(n, iteraciones=50):
    if n < 0:
        print(' Error: No existe raiz cuadrada de un numero negativo.')
        return None
    if n == 0:
        return 0
    estimacion = n / 2.0
    for i in range(iteraciones):
        estimacion = (estimacion + n / estimacion) / 2.0
    return estimacion


# Exponencial
def exponencial(x, terminos=50):
    resultado = 0.0
    termino_actual = 1.0
    for i in range(1, terminos + 1):
        resultado = resultado + termino_actual
        termino_actual = termino_actual * x / i
    return resultado


# Seno
def seno(x, terminos=15):
    resultado = 0.0
    termino_actual = x
    for i in range(terminos):
        resultado = resultado + termino_actual
        n = 2 * i + 2
        termino_actual = termino_actual * (-1) * x * x / (n * (n + 1))
    return resultado

# Coseno
def coseno(x, terminos=15):
    resultado = 0.0
    termino_actual = 1.0  # primer término es 1
    for i in range(terminos):
        resultado = resultado + termino_actual
        # Cada nuevo término: multiplica por -x² / ((2i+1)*(2i+2))
        n = 2 * i + 1
        termino_actual = termino_actual * (-1) * x * x / (n * (n + 1))
    return resultado


# Logaritmo Natural
def logaritmo(x, terminos=100):
    if x <= 0:
        print(' Error: El logaritmo solo existe para x > 0.')
        return None
    u = (x - 1) / (x + 1)
    resultado = 0.0
    u_potencia = u  # empieza con u^1
    for i in range(terminos):
        divisor = 2 * i + 1  # denominadores impares: 1, 3, 5, 7, ...
        resultado = resultado + u_potencia / divisor
        u_potencia = u_potencia * u * u  # sube dos potencias: u³, u⁵, ...
    return 2 * resultado
