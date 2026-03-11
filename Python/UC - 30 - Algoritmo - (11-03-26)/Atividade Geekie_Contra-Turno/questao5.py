escola = {}

escola["nome"] = input("Nome? ")
escola["mat"] = int(input("Matrícula? "))
escola["nota1"] = float(input("Nota 1? "))
escola["nota2"] = float(input("Nota 2? "))

media = (escola["nota1"] + escola["nota2"])/ 2

print("Sua média é: ", media)