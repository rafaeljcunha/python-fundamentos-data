perguntas = [
    {
        "titulo": "Quanto é 2 + 2?",
        "opcoes": {
            "a": "5",
            "b": "4"
        },
        "opcaoCorreta": "b"
    },
    {
        "titulo": "Quanto é 2 + 5?",
        "opcoes": {
            "a": "4",
            "b": "7"
        },
        "opcaoCorreta": "b"
    },
    {
        "titulo": "4 = X. Quais os possível valores de X:",
        "opcoes": {
            "a": "2^2",
            "b": "-2 * 2",
            "c": "2 * 2",
            "d": "4^1"
        },
        "opcaoCorreta": "abd"
    }
]

def exibir_perguntas(questao):
    print(questao["titulo"])
    for opcao, texto in questao["opcoes"].items():
        print(f"{opcao}. {texto}")
    resposta = input("Resposta do usuário: ").lower()
    return resposta

def executar_quiz(questoes):
    pontuacao = 0
    for questao in questoes:
        resposta_usuario = exibir_perguntas(questao)
        if resposta_usuario == questao["opcaoCorreta"]:
            pontuacao += 1
    print(f"Você acertou {pontuacao}/{len(questoes)} respostas.")

print("Bem vindo ao Quiz Decola.")
print(f"Esse quiz é composto por {len(perguntas)} Questões.")
executar_quiz(perguntas)
