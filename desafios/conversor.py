print("Escolha uma opção para converter:")
print("1 - Conveter Graus Celsius para Kelvin")
print("2 - Conveter Graus Celsius para Fahrenheit")
print("3 - Conveter Real para Dólar")
print("4 - Conveter Real para Euro")
opcaoSelecionada = int(input("Digite a sua opção: "))
valorParaConverter = float(input("Digite o valor a converter: "))

kelvin = valorParaConverter + 273.15
fahrenheit = (valorParaConverter * 9/5) + 32
dolar = valorParaConverter * 0.2
euro = valorParaConverter * 0.19

match opcaoSelecionada:
    case 1:
        print("A conversão é:", kelvin)
    case 2:
        print("A conversão é:", fahrenheit)
    case 3:
        print("A conversão é:", dolar)
    case 4:
        print("A conversão é:", euro)
    case _:
        print("Opção inválida.")
