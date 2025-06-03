import json
import csv
from processamento_dados import Dado

#Caminho dos arquivos da empresa A e B
path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

print("Iniciando a leitura dos arquivos")
print(".......................................................................")
empresaA = Dado(path_json, 'json')
print("Dados da empresa A lidos.")
print(".......................................................................")
empresaB = Dado(path_csv, "csv")
print("Dados da empresa B lidos.")
print(".......................................................................")
print("Dados da empresa A:")
print(empresaA.nome_colunas)
print(empresaA.tamanho)
print("Dados da empresa B:")
print(empresaB.nome_colunas)
print(empresaB.tamanho)
print(".......................................................................")
print("Iniciado as tranformações dos dados.")
key_map = {'Nome do Item':'Nome do Produto', 
           'Classificação do Produto':'Categoria do Produto', 
           'Valor em Reais (R$)': 'Preço do Produto (R$)',
           'Quantidade em Estoque': 'Quantidade em Estoque',
           'Nome da Loja':'Filial',
           'Data da Venda':'Data da Venda'
           }

empresaB.renomear(key_map)
print("Colunas renomeadas.")

dados_fusao = Dado.juntar(empresaA, empresaB)
print("Informacoes foram combinadas.")
print(".......................................................................")
print("Salvando as informações.")
path_salvar = '../data_processed/dados_combinados.csv'
dados_fusao.salvar(path_salvar)
print("As informações foram salvas na pasta 'data_processed'.")