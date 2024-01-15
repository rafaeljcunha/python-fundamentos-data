import csv

dados_gerais = [
  ["id", "nome", "horas", "valor"],
  [1, "Claython", 180, 10.5],
  [2, "Winx", 181, 11],
  [3, "Vou ver e te aviso", 176, 19.3],
  [4, "Eu sou o Douglas", 200, 21.1]
]

def calcular_horas(horas: int, valorHora: float) -> None:
  horasExcedentes: int = horas - 176
  valorHoras: float = (horas - horasExcedentes) * valorHora
  valorHorasExcedentes: float = horasExcedentes * (valorHora * 1.5)
  valorPagar: float = valorHoras + valorHorasExcedentes
  return valorPagar

with open("dados_horas_funcionarios.csv", "w", newline="") as planilha:
  escrever_planilha = csv.writer(planilha, delimiter=";")
  for linha in dados_gerais:
    escrever_planilha.writerow(linha)

dados_planilha_horas = [
  ["id", "valor"]
]
with open("dados_horas_funcionarios.csv", "r") as planilha_criada:
    ler_planilha = csv.reader(planilha_criada, delimiter=";")
    for linha in ler_planilha:
      if linha[0] != "id" and linha[3] != "valor":
        funcionarioId = int(linha[0])
        funcionarioHoras = int(linha[2])
        funcionarioValorHora = float(linha[3])
       
        with open("dados_pagar_horas.csv", "w", newline="") as planilha_horas:
          valorPagar = calcular_horas(funcionarioHoras, funcionarioValorHora)
          dados_planilha_horas.append([funcionarioId, round(valorPagar, 2)])
          escrever_planilha_horas = csv.writer(planilha_horas, delimiter=";")
          for linha_funcionario in dados_planilha_horas:
            escrever_planilha_horas.writerow(linha_funcionario)