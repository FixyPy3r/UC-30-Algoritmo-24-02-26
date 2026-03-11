base = 3500
desconto = -250
bonus = 800
bruto = base + bonus
liquido = bruto - desconto

print("Seu salario bruto é de: ", bruto)
print("Seu salario liquido será: ", liquido)

print(type(base))
print(type(desconto))
print(type(bonus))
print(type(bruto))
print(type(liquido))