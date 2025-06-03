import json
import csv

#Caminho dos arquivos da empresa A e B
path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

#Lendo o arquivo da empresa A em formato JSON
print("Iniciando a leitura dos arquivos")
print(".......................................................................")
with open(path_json, 'r') as file:
    dados_js = json.load(file)
print("Dados da empresa A lidos.")
print(".......................................................................")

#Lendo o arquivo da empresa B no formato lista de dicionarios
dados_csv = []
with open(path_csv, 'r') as file:
    reader = csv.DictReader(file, delimiter=',')

    for row in reader:
        dados_csv.append(row)
print("Dados da empresa B lidos.")
print(".......................................................................")

#Informacoes sobre os arquivos
colunas_json = list(dados_js[0].keys())
colunas_csv = list(dados_csv[0].keys())

print(f"Nomes das colunas aquivo json: \n {colunas_json}")
print(".......................................................................")
print(f"Nomes das colunas aquivo csv: \n {colunas_csv}")
print(".......................................................................")
tamanho_js = len(dados_js)
tamanho_csv = len(dados_csv)
print(f"Total registros js: {tamanho_js}")
print(f"Total registros csv: {tamanho_csv}")
print(".......................................................................")

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

new_dados_csv = []
for old in dados_csv:
    temp = {}

    for key, value in old.items():
        temp[key_map[key]] = value
    
    new_dados_csv.append(temp)

print("Colunas renomeadas.")
#Juntando as informacoes, ja lidando com a quantidade menor de colunas
lista_combinada = []
lista_combinada.extend(dados_js)
lista_combinada.extend(new_dados_csv)
nome_colunas = list(lista_combinada[-1].keys())

dados_combinados_tabela = [nome_colunas]

for row in lista_combinada:
    linha = []
    for colu in nome_colunas:
        linha.append(row.get(colu, "Indisponivel"))
    
    dados_combinados_tabela.append(linha)

print("Informacoes foram combinadas. Aparecerá 'Indisponível' para a informacao de data que não consta no arquivo da empresa A")
print(".......................................................................")

#Salvando as informacoes na pasta data_processed
print("Salvando as informações.")
path_salvar = '../data_processed/dados_combinados.csv'

with open(path_salvar, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(dados_combinados_tabela)

print("As informações foram salvas na pasta 'data_processed'.")