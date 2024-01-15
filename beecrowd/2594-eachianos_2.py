import re

def EncontrarPosicoes(texto, palavra):
    posicoes = [match.start() for match in re.finditer(r'\b{}\b'.format(re.escape(palavra)), texto)]
    return posicoes

quantidadeTextos = int(input())

for i in range(quantidadeTextos):
    texto = input()
    palavra = input()
    posicoes = EncontrarPosicoes(texto, palavra)
    if len(posicoes) > 0:
        print(" ".join(map(str, posicoes)))
    else:
        print(-1)