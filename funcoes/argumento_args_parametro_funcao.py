def MultiplicaArgs(*args):
    """A sintaxe *args quando incluída em uma função determina que é possível passar um número variável de argumentos, sem uma palavra-chave e de comprimento também variável"""
    resultado = 1
    for i in args:
        resultado *= i
    return print(resultado)

MultiplicaArgs(2,4,9,150,4)
MultiplicaArgs(5,4)
MultiplicaArgs(2)