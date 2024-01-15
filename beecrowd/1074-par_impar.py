casos_teste = int(input())

for _ in range(casos_teste):
    valor = int(input())
    if valor == 0:
        print("NULL")
    else:
        if valor % 2 == 0:
            print("EVEN", end=" ")
        else:
            print("ODD", end=" ")
        
        if valor > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")
        
        