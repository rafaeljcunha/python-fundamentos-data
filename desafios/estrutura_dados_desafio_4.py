lista = []
while True:
  personalInfo = {}

  nome = input("Informe o nome: ")
  personalInfo["nome"] = nome

  if(personalInfo["nome"] == ""):
    print(lista)
    for item in lista:
      print(f'{item["nome"]}, possui {item["idade"]} anos e mora em {item["cidade"]}.')
    break

  idade = input("Informe a idade: ")
  personalInfo["idade"] = idade

  cidade = input("Informe a cidade: ")
  personalInfo["cidade"] = cidade

  lista.append(personalInfo)
