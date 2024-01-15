valor = 0

try:
    valor = int(input("Digite a sua idade: "))
except ValueError as error:
    print("Não foi possível ler sua idade, use somente números:", error)
else:
    print("Sua idade é:", valor, "anos")
