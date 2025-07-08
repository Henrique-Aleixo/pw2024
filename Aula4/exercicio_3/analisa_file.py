import os

def pede_pasta():
    """Pede o caminho de uma pasta para analisar e verifica se existe."""
    while True:
        caminho = input("Insira o caminho da pasta para analisar: ")
        if os.path.isdir(caminho):
            return caminho
        else:
            print("Pasta não encontrada. Tente novamente.")

def calcula_tamanho_pasta(pasta):
    """Calcula o tamanho total em bytes dos ficheiros numa pasta e suas sub-pastas (recursivamente)."""
    soma = 0
    
    try:
        # Itera pelos elementos da pasta
        for elemento in os.listdir(pasta):
            # Constrói o caminho absoluto
            caminho_completo = os.path.join(pasta, elemento)
            
            # Se for um ficheiro, adiciona o seu tamanho
            if os.path.isfile(caminho_completo):
                soma += os.path.getsize(caminho_completo)
            
            # Se for uma pasta, chama recursivamente a função
            if os.path.isdir(caminho_completo):
                soma += calcula_tamanho_pasta(caminho_completo)
                
    except PermissionError:
        # Ignora pastas sem permissão de acesso
        print(f"Sem permissão para aceder a: {pasta}")
    except Exception as e:
        # Ignora outros erros
        print(f"Erro ao aceder a {pasta}: {e}")
    
    return soma

def main():
    """Função principal que executa o programa."""
    # Pede o caminho da pasta
    pasta = pede_pasta()
    
    # Calcula o tamanho total
    tamanho_bytes = calcula_tamanho_pasta(pasta)
    
    # Converte para MBytes
    tamanho_mbytes = tamanho_bytes / (1024 * 1024)
    
    # Imprime o resultado
    print(f"Tamanho total da pasta '{pasta}' e suas sub-pastas: {tamanho_mbytes:.2f} MBytes")

if __name__ == "__main__":
    main()
