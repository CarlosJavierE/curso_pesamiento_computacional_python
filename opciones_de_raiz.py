def enumeracion():
    objetivo = int(input("Escribe un numero: "))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        print(respuesta) #esto es opcional para ver como funciona el programa
        respuesta += 1

    if respuesta **  2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene raiz cuadrada exacta")


def aproximacion():
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta ** 2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def busqueda_binaria():
    objetivo = int(input('Escribe un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'La raiza cuadra de {objetivo} es {respuesta}')


def run():
    menu = """
    Hola Bienvenido, para hallar la raiz cuadrada elija un metodo

    1 - Enumeracion Exhustiva
    2 - Por aproximacion
    3 - Busqueda Binaria
    
    Elija una opcion: """

    opcion = int(input(menu))

    if opcion == 1:
        enumeracion()
    elif opcion == 2:
        aproximacion()
    elif opcion == 3:
        busqueda_binaria()
    else:
        print('Elija una opcion correcta por favor')


if __name__ == '__main__':
    run()