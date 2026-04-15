def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida")
        return 0

soma_segura("a", 2)

def divisao(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return print("Não divida por zero!")
    
divisao(10, 0)