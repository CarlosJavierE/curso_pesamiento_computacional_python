nombre1 = input("Escriba un nombre:")
edad1 = int(input("Escriba su edad: "))

nombre2 = input("Escriba un nombre: ")
edad2 = int(input("Escriba su edad: "))

if edad1 > edad2:
    # nota!! aqui se puede porner o no la str(edad1) para que lo imprima en pantalla
    # al paracer para 'print' no es necesario poner las str por no tiene las mismas funciones que 'input'
    print(f"{nombre1} es mayor con {str(edad1)} que {nombre2} con {str(edad2)}")
elif edad1 < edad2:
    print(f"{nombre2} es mayor con {edad2} que {nombre1} con {edad1}")
else:
    print("Las dos personas tienen la misma edad")
    