nombre1 = input("Escriba un nombre: ")
edad1 = int(input("Escriba la edad: "))

nombre2 = input("Escriba un nombre: ")
edad2 = int(input("Escriba la edad: "))

if edad1 > edad2:
    print(f'{nombre1} es mayor con {edad1} que {nombre2} con {edad2}')
elif edad1 < edad1:
    print(f'{nombre2} es mayor con {edad2} que {nombre1} con {edad1}')
else:
    print('Los dos tienen la misma edad')