objetivo = int(input("Escribe un numero: "))
respuesta = 0

while respuesta ** 2 < objetivo:
    print(respuesta) #esto es opcional para ver como funciona el programa
    respuesta += 1

if respuesta **  2 == objetivo:
    print(f"La raiz cuadrada de {objetivo} es {respuesta}")
else:
    print(f"{objetivo} no tiene raiz cuadrada exacta")