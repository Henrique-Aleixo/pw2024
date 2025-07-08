def calcula_linhas(nome_ficheiro):
    """Retorna o número de linhas do ficheiro."""
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        return len(ficheiro.readlines())

def calcula_carateres(nome_ficheiro):
    """Retorna o número de caracteres do ficheiro."""
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        return len(ficheiro.read())

def calcula_palavra_comprida(nome_ficheiro):
    """Retorna a palavra mais comprida do ficheiro."""
    palavra_mais_comprida = ""
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        for linha in ficheiro:
            palavras = linha.split()
            for palavra in palavras:
                if len(palavra) > len(palavra_mais_comprida):
                    palavra_mais_comprida = palavra
    return palavra_mais_comprida

def calcula_ocorrencia_de_letras(nome_ficheiro):
    """Cria um dicionário com a frequência de todas as letras do ficheiro."""
    frequencias = {}
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        conteudo = ficheiro.read().lower()
        for caracter in conteudo:
            if caracter.isalpha():
                frequencias[caracter] = frequencias.get(caracter, 0) + 1
    return frequencias
