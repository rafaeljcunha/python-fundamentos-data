import csv

quiz_data = {}

with open('dados_quiz.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        questao_id = int(row['id_questao'])
        if questao_id not in quiz_data:
            quiz_data[questao_id] = {'pergunta': row['texto_questao'], 'opcoes': [], 'respostas_corretas': []}

        quiz_data[questao_id]['opcoes'].append(f"{row['letra_alternativa']}. {row['texto_alternativa']}")
        if row['alternativa_correta'] == "correta":
            quiz_data[questao_id]['respostas_corretas'].append(row['letra_alternativa'])

acertos = 0

print("Bem-vindo ao Quiz Decola.")
print(f"Esse quiz é composto por {len(quiz_data)} Questões.\n")

for num_questao, questao_info in quiz_data.items():
    print(f"{num_questao}. {questao_info['pergunta']}")
    for opcao in questao_info['opcoes']:
        print(opcao)

    resposta_usuario = input("Resposta do usuário: ").lower()

    respostas_corretas = "".join(sorted(questao_info['respostas_corretas']))
    resposta_usuario = "".join(sorted(resposta_usuario))

    if resposta_usuario == respostas_corretas:
        acertos += 1
    print()

print(f"Você acertou {acertos}/{len(quiz_data)} respostas.")