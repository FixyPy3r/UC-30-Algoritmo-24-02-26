#Gere uma função que mostre a soma e o produto de dois números
def someeprodute(soma1, soma2):
    soma = soma1 + soma2
    produto = soma1 * soma2
    return soma, produto

resultado = someeprodute(8.0, 9.0)
print(f"Soma e produto, respectivamente {resultado}")