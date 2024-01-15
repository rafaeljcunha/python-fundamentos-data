lista = ["Rafael", 30, 1]

lista.extend(["Bryant", "Nathalya"]) # Método extend
# Extend adiciona os elementos a lista original
print(lista)

lista.append(3) # Método append
lista.append(26)
print(lista)

lista.append(["Bryant", "Nathalya"]) # Método append lista
# Se usar o append para adicionar elementos a partir de uma lista
# toda a lista será adicionada, criando uma lista aninhada, ao contrário
# do extend, que adiciona apenas os elementos da lista, dentro de outra lista
