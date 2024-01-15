import csv
import requests

dados_gerais = [
  ["id", "dias", "cidade"],
  [1, 7, "Lisboa"],
  [2, 5, "Lisboa"],
  [3, 3, "Amsterdam"],
  [4, 8, "Amsterdam"],
  [5, 2, "Roma"],
  [6, 10, "Paris"],
  [7, 3, "Paris"]
]

response = requests.get("https://open.er-api.com/v6/latest/EUR")
resultado = response.json()
valor_real = resultado["rates"]["BRL"]

def aluguel_carro(dias: int) -> float:
  diaria = 40
  desconto_medio = 20
  desconto_integral = 50

  if dias >= 3 and dias < 7:
   return (diaria * dias) - desconto_medio
  if dias >= 7:
   return (diaria * dias) - desconto_integral
  return diaria

def estadias_hotel(dias: int) -> float:
  diaria_hotel = 150
  return dias * diaria_hotel

def custo_alimentacao(dias: int, local: str) -> float:
  dict_custo_alimentacao = {}
  dict_custo_alimentacao["Paris"] = 50
  dict_custo_alimentacao["Amsterdam"] = 80
  dict_custo_alimentacao["Lisboa"] = 30
  dict_custo_alimentacao["Roma"] = 45

  return dias * dict_custo_alimentacao[local]

with open("dados_estadias.csv", "w", newline="") as dados_estadias:
  escrever_dados = csv.writer(dados_estadias, delimiter=";")
  for linha in dados_gerais:
    escrever_dados.writerow(linha)

dados_valores = [
  ["id", "valor_real", "valor_euro"]
]
with open("dados_estadias.csv", "r") as ler_dados_estadias:
  ler_estadias = csv.reader(ler_dados_estadias, delimiter=";")
  for linha in ler_estadias:
    dias_estadia = linha[1]
    if dias_estadia != "dias":
      local = linha[2]
      localId = int(linha[0])
      with open("dados_valores_estadias.csv", "w", newline="") as dados_valores_estadias:
        aluguel = aluguel_carro(int(dias_estadia))
        estadia = estadias_hotel(int(dias_estadia))
        alimentacao = custo_alimentacao(int(dias_estadia), local)
        
        total_euros = aluguel + estadia + alimentacao
        total_reais = total_euros * valor_real

        dados_valores.append([localId, round(total_reais), round(total_euros)])
        valores_estadias = csv.writer(dados_valores_estadias, delimiter=";")
        for valores in dados_valores:
          valores_estadias.writerow(valores)
