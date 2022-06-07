def enumeracion():
    objetivo = int(input("Escriba un numero entero:"))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        # print(respuesta)
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} No tiene raiz exacta')


def aproximacion():
    objetivo = int(input("Escriba un numero entero: "))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta < objetivo:
        # print(respuesta) # opcional
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f"No se encontro la raiz de {objetivo}")
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria():
    objetivo = int(input("Escriba un numero: "))
    epsilon = 0.01
    bajo = 0
    alto = max(1.0 , objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        # print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')



def run():
    opcion = int(input(menu))
    if opcion == 1:
        enumeracion()
    elif opcion == 2:
        aproximacion()
    elif opcion == 3:
        busqueda_binaria()
    else:
        print("POR FAVOR ELIJA UNA OPCION CORRECTA")


menu = """
BIENVENIDO A LA APLICACION
1 - Raiz por enumeracion exhaustiva
2 - Raiz por aproxiacion
3 - Raiz por busqueda binaria

Elija una opcion: """


if __name__ == '__main__':
    run()