import random

print("Adivinhe o número")
print("É um número de 1 à 100")
print("Adivinhe")

nreal = random.randint(1, 100)
tentativas = 0
acertou = False

while acertou == False:
    chute = int(input("Seu chute: "))
    tentativas = tentativas + 1

    if chute < nreal:
        print("Errou! O numero e MAIOR.")
    elif chute > nreal:
        print("Errou! O numero e MENOR.")
    else:
        print("Acertou! O numero era", nreal)
        print("Voce usou", tentativas, "tentativas.")
        acertou = True

print("Repetição dos números")
print("Digite 8 numeros:")

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))
numero4 = int(input("Numero 4: "))
numero5 = int(input("Numero 5: "))
numero6 = int(input("Numero 6: "))
numero7 = int(input("Numero 7: "))
numero8 = int(input("Numero 8: "))

lista = [numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8]

print("Voce digitou:", lista)

print("Resultado")

repetido = False

for numero in lista:
    quantidade = lista.count(numero)

    if quantidade > 1:
        repetido = True

if repetido == False:
    print("Nenhum numero foi repetido.")
else:
    n = []

    for numero in lista:
        quantidade = lista.count(numero)

        if quantidade > 1 and numero not in n:
            print("O numero", numero, "apareceu", quantidade, "vezes.")
            n.append(numero)