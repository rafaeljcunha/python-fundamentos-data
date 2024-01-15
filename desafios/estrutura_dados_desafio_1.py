lista = [12, -2, 4, 8, 29, 45, 78, 36, -7, 2, 12, 8, 3, 3, -52]

# Imprima o maior elemento
print("Imprima o maior elemento: ", max(lista))

# Imprima o menor elemento
print("Imprima o menor elemento: ", min(lista))

# Imprima os números pares
print("Imprima os números pares:")
for valor in lista:
    if(valor % 2 == 0):
      print(valor)

# Imprima o número de ocorrências do primeiro elemento da lista
ocorrencias = []
for valor in lista:
   if(valor == lista[0]):
      ocorrencias.append(valor)
print("Imprima o número de ocorrências do primeiro elemento da lista: ", len(ocorrencias))

# Imprima a média dos elementos
total = sum(lista)
media = total / len(lista)
print("Imprima a média dos elementos: ", media)

# Imprima a soma dos elementos de valor negativo
somaValorNegativo = 0
for valor in lista:
  if(valor < 0):
    somaValorNegativo += valor
print("Imprima a soma dos elementos de valor negativo: ", somaValorNegativo)