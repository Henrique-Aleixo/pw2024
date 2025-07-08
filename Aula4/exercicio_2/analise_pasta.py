import os
import csv
import matplotlib.pyplot as plt

def pede_pasta():
    """Pede ao utilizador para inserir um caminho para uma pasta."""
    while True:
        caminho = input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta: ")
        if os.path.isdir(caminho):
            return caminho
        else:
            print("Pasta não encontrada. Tente novamente.")

def faz_calculos(caminho_pasta):
    """Contabiliza a quantidade de ficheiros e volume total ocupado por tipo de extensão."""
    dic_info = {}
    
    # Lista todos os itens na pasta
    for item in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, item)
        
        # Verifica se é um ficheiro (não pasta)
        if os.path.isfile(caminho_completo):
            # Obtém a extensão do ficheiro
            if '.' in item:
                extensao = item.split('.')[-1].lower()
            else:
                extensao = 'sem_extensao'
            
            # Obtém o tamanho do ficheiro em bytes
            tamanho_bytes = os.path.getsize(caminho_completo)
            tamanho_kbytes = tamanho_bytes / 1024  # Converter para kBytes
            
            # Adiciona ao dicionário
            if extensao not in dic_info:
                dic_info[extensao] = {'volume': 0, 'quantidade': 0}
            
            dic_info[extensao]['quantidade'] += 1
            dic_info[extensao]['volume'] += tamanho_kbytes
    
    return dic_info

def guarda_resultados(dic_info, caminho_pasta):
    """Guarda a informação num ficheiro CSV."""
    # Obtém o nome da pasta
    nome_pasta = os.path.basename(caminho_pasta)
    nome_ficheiro = f"{nome_pasta}.csv"
    
    # Escreve o ficheiro CSV
    with open(nome_ficheiro, 'w', newline='', encoding='utf-8') as ficheiro:
        campos = ['Extensao', 'Quantidade', 'Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        
        for extensao, info in dic_info.items():
            writer.writerow({
                'Extensao': extensao,
                'Quantidade': info['quantidade'],
                'Tamanho[kByte]': round(info['volume'])
            })
    
    print(f"Os resultados foram guardados no ficheiro `{nome_ficheiro}`")
    return nome_ficheiro

def faz_grafico_queijos(dic_info, nome_pasta):
    """Cria um gráfico de queijos (pie chart) com os resultados."""
    extensoes = list(dic_info.keys())
    volumes = [info['volume'] for info in dic_info.values()]
    
    plt.figure(figsize=(10, 8))
    plt.pie(volumes, labels=extensoes, autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribuição de Volume por Tipo de Ficheiro - {nome_pasta}')
    plt.axis('equal')
    plt.show()

def faz_grafico_barras(dic_info, nome_pasta):
    """Cria um gráfico de barras com os resultados."""
    extensoes = list(dic_info.keys())
    quantidades = [info['quantidade'] for info in dic_info.values()]
    
    plt.figure(figsize=(12, 6))
    plt.bar(extensoes, quantidades, color='skyblue')
    plt.title(f'Quantidade de Ficheiros por Tipo - {nome_pasta}')
    plt.xlabel('Extensão')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
