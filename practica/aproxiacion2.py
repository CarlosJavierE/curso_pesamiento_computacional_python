objetivo = int(input("Escriba un numero entero: "))
epsilon = 0.01
paso = epsilon ** 2
respuesta = 0

while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta < objetivo:
    print(respuesta) # opcional
    respuesta += paso

if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f"No se encontro la raiz de {objetivo}")
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')