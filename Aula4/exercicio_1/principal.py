import json
from analisa_ficheiro import acessorio, calculos

def main():
    """Função principal que executa a análise do ficheiro."""
    # Pede o nome do ficheiro
    nome_ficheiro = acessorio.pede_nome()
    
    # Gera o nome do ficheiro de resultados
    nome_resultado = acessorio.gera_nome(nome_ficheiro)
    
    # Calcula todas as estatísticas
    num_linhas = calculos.calcula_linhas(nome_ficheiro)
    num_carateres = calculos.calcula_carateres(nome_ficheiro)
    palavra_comprida = calculos.calcula_palavra_comprida(nome_ficheiro)
    ocorrencia_letras = calculos.calcula_ocorrencia_de_letras(nome_ficheiro)
    
    # Cria o dicionário com os resultados
    resultados = {
        "ficheiro_analisado": nome_ficheiro,
        "numero_linhas": num_linhas,
        "numero_carateres": num_carateres,
        "palavra_mais_comprida": palavra_comprida,
        "frequencia_letras": ocorrencia_letras
    }
    
    # Guarda os resultados em formato JSON
    with open(nome_resultado, 'w', encoding='utf-8') as ficheiro_json:
        json.dump(resultados, ficheiro_json, ensure_ascii=False, indent=4)
    
    print(f"Análise concluída! Resultados guardados em {nome_resultado}")

if __name__ == "__main__":
    main()
