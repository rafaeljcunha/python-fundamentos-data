lista = [1,2,["pop","rock"],[3,4],["disco",[1,2]]]
tupla = (1,2,("pop","rock"),(3,4),("disco",(1,2)))

# Lista
print("Elemento 2, da Lista 0: ",lista[2][0])
print("Elemento 2, da Lista 1: ",lista[2][1])
print("Elemento 3, da Lista 0: ",lista[3][0])
print("Elemento 3, da Lista 1: ",lista[3][1])
print("Elemento 4, da Lista 0: ",lista[4][0])
print("Elemento 4, da Lista 1: ",lista[4][1])

print("Elemento 2, da Tupla 0: ",tupla[2][0])
print("Elemento 2, da Tupla 1: ",tupla[2][1])
print("Elemento 3, da Tupla 0: ",tupla[3][0])
print("Elemento 3, da Tupla 1: ",tupla[3][1])
print("Elemento 4, da Tupla 0: ",tupla[4][0])
print("Elemento 4, da Tupla 1: ",tupla[4][1])


print("Elemento 1, da Segunda Lista Aninhada: ",lista[2][1][0])
print("Elemento 1, da Segunda Tupla Aninhada: ",tupla[2][1][0])
