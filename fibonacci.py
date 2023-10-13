### funcion generada con AI ###
 
def fibonacci(n, callback):
    a, b = 0, 1
    for i in range(n):
        callback(a)
        a, b = b, a + b

def imprimir_numero(numero):
    print(numero)

fibonacci(10, imprimir_numero)