import Operaciones_Basicas as ob
import Operaciones_Cientificas as oc
import Graficadora as gr
import Historial as hist

def mostrar_menu():
    print('   CALCULADORA CIENTIFICA GRAFICADORA')
    print('-' * 40)
    print('1. Operaciones basicas')
    print('2. Operaciones científicas')
    print('3. Evaluar una funcion')
    print('4. Graficar una funcion en consola')
    print('5. Ver historial de operaciones')
    print('6. Salir')


# Operaciones Basicas
def menu_basicas():
    print("\n Operaciones Básicas")
    print("  1. Suma")
    print("  2. Resta")
    print("  3. Multiplicacion")
    print("  4. Division")
    print("  5. Potencia")
    print("  6. Volver")

    opcion = input('Seleccione: ')

    if opcion == "6":
        return

    if opcion in ["1", "2", "3", "4"]:
        a = float(input(' Ingrese el primer numero: '))
        b = float(input(' Ingrese el segundo numero: '))
    elif opcion == "5":
        a = float(input(' Ingrese la base: '))
        b = int(input(' Ingrese el exponente (entero >= 0): '))
    else:
        print('Opcion no valida.')
        return

    if opcion == "1":
        resultado = ob.sumar(a, b)
        texto = f"Suma: {a} + {b} = {resultado}"

    elif opcion == "2":
        resultado = ob.restar(a, b)
        texto = f"Resta: {a} - {b} = {resultado}"

    elif opcion == "3":
        resultado = ob.multiplicar(a, b)
        texto = f"Multiplicacion: {a} * {b} = {resultado}"

    elif opcion == "4":
        resultado = ob.dividir(a, b)
        if resultado is None:
            return
        texto = f"Division: {a} / {b} = {resultado}"

    elif opcion == "5":
        resultado = ob.potencia(a, b)
        if resultado is None:
            return
        texto = f"Potencia: {a}^{b} = {resultado}"

    print(f"\n  Resultado: {resultado}")
    hist.agregar(texto)


# Operaciones Cientificas
def menu_cientificas():
    print('\n  --- Operaciones Cientificas ---')
    print('  1. Factorial  (n!)')
    print('  2. Raiz cuadrada')
    print('  3. Exponencial  (e^x)')
    print('  4. Seno  (radianes)')
    print('  5. Coseno  (radianes)')
    print('  6. Logaritmo natural  ln(x)')
    print('  7. Volver')

    opcion = input(' Seleccione: ')

    if opcion == "7":
        return

    if opcion == "1":
        n = int(input(' Ingrese n (entero >= 0): '))
        resultado = oc.factorial(n)
        if resultado is None:
            return
        texto = f"Factorial: {n}! = {resultado}"

    elif opcion == "2":
        x = float(input(' Ingrese el numero: '))
        resultado = oc.raiz_cuadrada(x)
        if resultado is None:
            return
        texto = f"Raiz cuadrada de {x} ≈ {resultado:.2f}"

    elif opcion == "3":
        x = float(input(' Ingrese x: '))
        resultado = oc.exponencial(x)
        texto = f"e^{x} ≈ {resultado:.2f}"

    elif opcion == "4":
        x = float(input(' Ingrese el angulo en radianes: '))
        resultado = oc.seno(x)
        texto = f"seno({x}) ≈ {resultado:.2f}"

    elif opcion == "5":
        x = float(input(' Ingrese el angulo en radianes: '))
        resultado = oc.coseno(x)
        texto = f"coseno({x}) ≈ {resultado:.2f}"

    elif opcion == "6":
        x = float(input(' Ingrese x (x > 0): '))
        resultado = oc.logaritmo(x)
        if resultado is None:
            return
        texto = f"ln({x}) ≈ {resultado:.2f}"

    else:
        print(' Opcion no válida.')
        return

    print(f"\n  Resultado: {resultado:.2f}")
    hist.agregar(texto)


# Evaluar Una Funcion  f(x)
funciones_eval = {
    "1": ("lineal     f(x) = 2x + 1", lambda x: 2 * x + 1),
    "2": ("cuadratica f(x) = x²", lambda x: x * x),
    "3": ("cubica     f(x) = x³", lambda x: x * x * x),
    "4": ("mixta      f(x) = x² + 2x + 1", lambda x: x * x + 2 * x + 1),
}

def menu_evaluar():
    print('\n Evaluar una Funcion')
    print(" Seleccione la funcion:")
    for clave in funciones_eval:
        nombre, _ = funciones_eval[clave]
        print(f"  {clave}. {nombre}")
    print(' 5. Volver')

    opcion = input(' Seleccione: ')

    if opcion == "5":
        return

    if opcion not in funciones_eval:
        print(' Opcion no valida.')
        return

    nombre_funcion, f = funciones_eval[opcion]
    x = float(input(' Ingrese el valor de x: '))
    resultado = f(x)

    print(f"\n  f({x}) = {resultado}")
    hist.agregar(f"Funcion {nombre_funcion.split()[0]}: f({x}) = {resultado}")


# Graficar Una Funcion
def menu_graficar():
    print('\nGraficar una Funcion en Consola')
    gr.mostrar_funciones_disponibles()

    nombre = input(' Escriba el nombre de la funcion: ').strip().lower()
    x_inicio = float(input(' Valor inicial de x (ejemplo -5): '))
    x_fin    = float(input(' Valor final de x   (ejemplo  5): '))

    if x_inicio >= x_fin:
        print(' Error: el valor inicial debe ser menor que el final.')
        return

    gr.graficar(nombre, x_inicio, x_fin)
    hist.agregar(f"Gráfica de '{nombre}' en [{x_inicio}, {x_fin}]")


# Bucle Del Programa
def main():
    opcion = ""
    while opcion != "6":
        mostrar_menu()
        opcion = input(' Seleccione una opcion: ').strip()

        if opcion == "1":
            menu_basicas()
        elif opcion == "2":
            menu_cientificas()
        elif opcion == "3":
            menu_evaluar()
        elif opcion == "4":
            menu_graficar()
        elif opcion == "5":
            hist.mostrar()
        elif opcion == "6":
            print("\n  ¡Hasta luego!\n")
        else:
            print(' Opción no valida, Intente de nuevo.')
main()
