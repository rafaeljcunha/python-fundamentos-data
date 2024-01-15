lista = []

while True:
  dadosInput = input("Informe um valor para a lista ou digite SAIR para encerrar: ")
  if(dadosInput.lower() == "sair"):
      break;
  lista.append(dadosInput)
  print("Sua lista: ", lista)