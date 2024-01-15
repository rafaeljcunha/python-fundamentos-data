N = int(input())

for _ in range(N):
    linha = input().strip()
    
    palavras = linha.split()
    
    mensagem_oculta = ""
    
    for palavra in palavras:
        if palavra:
            mensagem_oculta += palavra[0]
    
    print(mensagem_oculta)