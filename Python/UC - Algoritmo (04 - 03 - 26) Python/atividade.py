#Crie uma lista chamada COMPRAS com pelo menos 5 itens. Adicione um novo item à lista de forma que o usuario digite

compras = ["cebola, tomate, cenoura, alface, panela"]
print("Lista de Compras", compras)

compras.append("Molho") #adiciona no fim da lista
print("Lista atualizado: ", compras)

compras.insert(1, "Macarrão") #add em uma posição específica
print("Lista atualizado:", compras)

compras.extend(["Pão, Anchova"]) #add mais de um dado
print("Lista atualizado: ", compras)