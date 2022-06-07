# def primera_letra(lista_de_palabras):
#     primeras_letras = []

#     for palabra in lista_de_palabras:
#         assert type(palabra) == str, f'{palabra} no es str'
#         assert len(palabra) > 0, 'No se permiten str vacios'

#         primeras_letras.append(palabra[0])

#     return primeras_letras

# lista = ['hola', 50.3, 54, True, ""]
# print(primera_letra(lista))

def primera_letra(lista_palabras):
    primeras_letras = []
    
    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es String'
            assert len(palabra) > 0 , 'No se permiten vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras


lista = ['Angelo',5.5, '', 2 , '43952353', 0.35]
print('Primeras letras validas son : ' , primera_letra(lista))