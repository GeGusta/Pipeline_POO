import json
import csv

#Caminho dos arquivos da empresa A e B
path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

#Funcao para ler arquivos. Recebe o path do arquivo e tipo dele
def ler_arq(path, tipo):
    if tipo == "json":
        with open(path, 'r') as file:
            dados_js = json.load(file)

        return dados_js
    
    elif tipo == "csv":
        dados_csv = []
        with open(path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:
                dados_csv.append(row)
        
        return dados_csv
    
#Funcao para mostrar informacoes dos arquivos
def info_arq(arquivo):
    colunas_arq = list(arquivo[0].keys())
    print(f"Nomes das colunas aquivo: \n {colunas_arq}")
    print(".......................................................................")
    tamanho_arquivo = len(arquivo)
    print(f"Total registros: {tamanho_arquivo}")
    print(".......................................................................")

#Funcao para renomear as colunas
def renomear (arquivo, key_map):
    new_dados_csv = []
    for old in arquivo:
        temp = {}

        for key, value in old.items():
            temp[key_map[key]] = value
        
        new_dados_csv.append(temp)
    return new_dados_csv

#Funcao para juntar arquivos
def juntar (arq1, arq2):
    #Juntando as informacoes, ja lidando com a quantidade menor de colunas
    lista_combinada = []
    lista_combinada.extend(arq1)
    lista_combinada.extend(arq2)
    nome_colunas = list(lista_combinada[-1].keys())

    dados_combinados_tabela = [nome_colunas]

    for row in lista_combinada:
        linha = []
        for colu in nome_colunas:
            linha.append(row.get(colu, "Indisponivel"))
        
        dados_combinados_tabela.append(linha)
    
    return dados_combinados_tabela

def salvar(arq, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(arq)

print("Iniciando a leitura dos arquivos")
print(".......................................................................")
dados_js = ler_arq(path_json, 'json')
print("Dados da empresa A lidos.")
print(".......................................................................")
dados_csv = ler_arq(path_csv, 'csv')
print("Dados da empresa B lidos.")
print(".......................................................................")

info_arq(dados_js)
info_arq(dados_csv)

#Inicio da transformacao dos dados
#Mudanca dos nomes das colunas
#Mapa de troca de nome
print("Iniciado as tranformações dos dados.")
key_map = {'Nome do Item':'Nome do Produto', 
           'Classificação do Produto':'Categoria do Produto', 
           'Valor em Reais (R$)': 'Preço do Produto (R$)',
           'Quantidade em Estoque': 'Quantidade em Estoque',
           'Nome da Loja':'Filial',
           'Data da Venda':'Data da Venda'
           }

new_dados_csv = renomear(dados_csv, key_map)

print("Colunas renomeadas.")

dados_combinados = juntar(dados_js, new_dados_csv)

print("Informacoes foram combinadas. Aparecerá 'Indisponível' para a informacao de data que não consta no arquivo da empresa A")
print(".......................................................................")

#Salvando as informacoes na pasta data_processed
print("Salvando as informações.")
path_salvar = '../data_processed/dados_combinados.csv'

salvar(dados_combinados, path_salvar)
print("As informações foram salvas na pasta 'data_processed'.")