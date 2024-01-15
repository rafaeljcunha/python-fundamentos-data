personalInfo = {}
nome = input("Informe o seu nome: ")
personalInfo["Nome"] = nome

idade = input("Informe a sua idade: ")
personalInfo["Idade"] = idade

cidade = input("Informe a sua cidade: ")
personalInfo["Cidade"] = cidade

for key, value in personalInfo.items():
  print(f'{key}: {value}')