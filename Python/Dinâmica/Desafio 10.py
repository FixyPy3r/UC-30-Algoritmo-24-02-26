def numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
       return "Negativo"
    else:
        return "Zero"

print(numero(10))
print(numero(-2))
print(numero(0))