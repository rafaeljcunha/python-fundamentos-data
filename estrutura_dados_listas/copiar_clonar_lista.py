listaA = ["Rafael", 30, 1]
listaB = listaA.copy()

listaA[0] = "Bryant"
print(listaA)  # Modificado
print(listaB) # Original

# Copiar com fatiamento
listaC = listaB[:]
listaB[0] = "Nathalya"
print(listaB) # Modificado
print(listaC) # Original
