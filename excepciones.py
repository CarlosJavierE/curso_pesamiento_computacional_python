
def divide_elementos_de_lista(lista, divisor):
    # se puede poner adentro de la funcion de manera defensiva
    try:

        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        # 'as e' hace que ZeroDivisionError se ponga mas resumido
        print(e)
        return lista

lista = list(range(10))
divisor = 0


print(divide_elementos_de_lista(lista, divisor))

