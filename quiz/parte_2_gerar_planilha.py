import csv

dados_csv = [
  ["id_questao", "texto_questao", "id_alternativa", "letra_alternativa", "texto_alternativa", "alternativa_correta"],
  
  [1, "Quanto é 2 + 2?", 1, "a", "5", "incorreta"],
  [1, "Quanto é 2 + 2?", 2, "b", "4", "correta"],

  [2, "Quanto é 2 + 5?", 1, "a", "4", "incorreta"],
  [2, "Quanto é 2 + 5?", 2, "b", "7", "correta"],

  [3, "4 = X. Quais os possível valores de X:", 1, "a", "2ˆ2", "correta"],
  [3, "4 = X. Quais os possível valores de X:", 2, "b", "-2 * 2", "correta"],
  [3, "4 = X. Quais os possível valores de X:", 3, "c", "2 * 2", "incorreta"],
  [3, "4 = X. Quais os possível valores de X:", 4, "d", "4ˆ1", "correta"]
]

with open("dados_quiz.csv", "w", newline="") as planilha:
  escrever_planilha = csv.writer(planilha, delimiter=";")
  for linha in dados_csv:
    escrever_planilha.writerow(linha)