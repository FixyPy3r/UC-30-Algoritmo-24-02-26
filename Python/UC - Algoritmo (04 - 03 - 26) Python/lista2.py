animal = ["Cachorro, gato"]
print("Lista inicial", animal)

animal.append("Pato") #adiciona no fim da lista
print("Lista atualizado: ", animal)

animal.insert(1, "Coelho") #add em uma posição específica
print("Lista atualizado:", animal)

animal.extend(["macaco", "leão"]) #add mais de um dado
print("Lista atualizado: ", animal)

animal.remove("leão")
print(animal)

removido = animal.pop()
print(f"removido: {removido}")
print("Após pop()", animal)

removido2 = animal.pop(1)
print(f"Removido do índice 1 {removido2}")
print("Após pop(1): ", animal)

del animal[0]
print("Após o del", animal)

animal.clear()
print("Após o del", animal)
