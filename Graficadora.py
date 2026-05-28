funciones = {
    "lineal": lambda x: 2 * x + 1,
    "cuadratica": lambda x: x * x,
    "cubica": lambda x: x * x * x,
    "seno_aprox": lambda x: x - (x ** 3) / 6 + (x ** 5) / 120  # seno aproximado
}


def graficar(nombre_funcion, x_inicio=-5, x_fin=5, ancho=60, alto=20):

    if nombre_funcion not in funciones:
        print(f"  Funcion '{nombre_funcion}' no encontrada.")
        return

    f = funciones[nombre_funcion]

    valores_y = []
    paso_x = (x_fin - x_inicio) / ancho  

    for col in range(ancho):
        x = x_inicio + col * paso_x
        valores_y.append(f(x))

    y_min = valores_y[0]
    y_max = valores_y[0]
    for y in valores_y:
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y

    rango_y = y_max - y_min
    if rango_y == 0:
        rango_y = 1

    grid = []
    for fila in range(alto):
        fila_vacia = []
        for col in range(ancho):
            fila_vacia.append(' ')
        grid.append(fila_vacia)


    for col in range(ancho):
        y = valores_y[col]

        fila = int((y_max - y) / rango_y * (alto - 1))
        if 0 <= fila < alto:
            grid[fila][col] = '*'

    print(f"\n  Grafica de '{nombre_funcion}' en [{x_inicio}, {x_fin}]")
    print("  " + "-" * (ancho + 2))
    for fila in range(alto):
        linea = "".join(grid[fila])
        print(f"  |{linea}|")
    print("  " + "-" * (ancho + 2))
    print(f"  x: {x_inicio} {'':>{ancho - 10}} {x_fin}")
    print()


def mostrar_funciones_disponibles():
    print("\n  Funciones disponibles:")
    for nombre in funciones:
        print(f"    - {nombre}")
    print()
