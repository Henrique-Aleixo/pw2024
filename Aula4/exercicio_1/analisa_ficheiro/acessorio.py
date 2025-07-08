import os

def pede_nome():
    """Pede o nome de um ficheiro de texto e verifica se existe."""
    while True:
        nome_ficheiro = input("Introduza o nome do ficheiro de texto (com extensão .txt): ")
        if os.path.exists(nome_ficheiro):
            return nome_ficheiro
        else:
            print("Ficheiro não encontrado. Tente novamente.")

def gera_nome(nome_ficheiro):
    """Recebe o nome do ficheiro e cria o nome para guardar os resultados em formato JSON."""
    nome_base = nome_ficheiro.rsplit('.', 1)[0]
    return nome_base + ".json"
