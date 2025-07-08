import analise_pasta
import os

def main():
    """Função principal que executa a análise da pasta."""
    # Pede o caminho da pasta
    caminho_pasta = analise_pasta.pede_pasta()
    
    # Faz os cálculos
    dic_info = analise_pasta.faz_calculos(caminho_pasta)
    
    # Verifica se foram encontrados ficheiros
    if not dic_info:
        print("Nenhum ficheiro encontrado na pasta.")
        return
    
    # Guarda os resultados em CSV
    nome_ficheiro = analise_pasta.guarda_resultados(dic_info, caminho_pasta)
    
    # Obtém o nome da pasta para os gráficos
    nome_pasta = os.path.basename(caminho_pasta)
    
    # Cria os gráficos
    analise_pasta.faz_grafico_queijos(dic_info, nome_pasta)
    analise_pasta.faz_grafico_barras(dic_info, nome_pasta)

if __name__ == "__main__":
    main()
