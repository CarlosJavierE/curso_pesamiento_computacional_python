def factorial(n):
    """
    Calcula el Factorial de n.
    n int > 0
    returns n!
    """
    # lo de arriba sirve para saber de que va el programa
    # con la funcion 'help' se ve el contenido
    print(n) # nos sirve para ver como se mueve 'n'
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input("Escribe un entero: "))

print(factorial(n))