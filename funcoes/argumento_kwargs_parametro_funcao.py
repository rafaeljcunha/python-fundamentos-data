def funcionariosalario(**kwargs):
    """A sintaxe **kwargs quando incluída em uma função determina que é possível passar um número variável de argumentos, com palavras-chave e de comprimento também variável"""
    for key, value in kwargs.items():
        print ("%s = %s" %(key, value))

funcionariosalario(nome="João", sobrenome="Silva", salario=1000)
funcionariosalario(nome="Rafael", sobrenome="Juliani")