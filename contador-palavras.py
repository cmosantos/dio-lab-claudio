def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

entrada = "Este é um exemplo de texto para contar palavras."
print("Total de palavras:", contar_palavras(entrada))
