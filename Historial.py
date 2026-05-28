historial = []

def agregar(texto):
    historial.append(texto)


def mostrar():
    if len(historial) == 0:
        print(' El historial está vacío.')
    else:
        print('\nHISTORIAL DE OPERACIONES')
        for i in range(len(historial)):
            print(f"  {i + 1}. {historial[i]}")
        print()


def limpiar():
    historial.clear()
    print(' Historial borrado.')