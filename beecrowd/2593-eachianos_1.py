import re

texto = input()
quantidade_palavras = int(input())
palavras = input().split()

def encontrar_posicoes(texto, palavra):
    posicoes = [str(match.start()) for match in re.finditer(r'\b{}\b'.format(re.escape(palavra)), texto)]
    return posicoes

for palavra in palavras:
    posicoes = encontrar_posicoes(texto, palavra)
    if len(posicoes) > 0:
        print(" ".join(posicoes))
    else:
        print("-1")
