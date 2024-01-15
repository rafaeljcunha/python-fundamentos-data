print("FOR")
for letra in "Iteris":
    print(letra)

print("WHILE")
valor = input("Digite 'banana': ")
while valor.lower() != "banana":
    print("Você NÁO digitou banana")
    valor = input("Digite 'banana': ")
else:
    print("Você digitou banana")

print("if/else/elif")
valor = int(input("Digite um número entre 0 e 9: "))

if 0 <= valor and valor < 5:
    print("Número entre 0 e 4")
elif 5 <= valor and valor < 10:
    print("Número entre 5 e 9")
else:
    print("Número inválido escolhido")


print("match/case")  # Substituto do switch/case

valorMatch = int(input("Escolha uma das opções. De 1 à 3: "))
mensagem = ""

match valorMatch:
    case 1:
        mensagem = "Opção 1 escolhida"
    case 2:
        mensagem = "Opção 2 escolhida"
    case 3:
        mensagem = "Opção 3 escolhida"
    # default
    case _:
        mensagem = "Opção inválida"
print(mensagem)
