import json
import csv

class Dado:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.ler_arq()
        self.nome_colunas = self.info_colunas()
        self.tamanho = self.tamanho()

    #Metodo para ler o arquivo
    def ler_arq(self):
        if self.tipo_dados == "json":
            with open(self.path, 'r') as file:
                dados_js = json.load(file)

            return dados_js
        
        elif self.tipo_dados == "csv":
            dados_csv = []
            with open(self.path, 'r') as file:
                reader = csv.DictReader(file, delimiter=',')

                for row in reader:
                    dados_csv.append(row)
            
            return dados_csv
        
        elif self.tipo_dados == "lista":
            dados = self.path
            self.path = "Lista de memoria"
        
        return dados

    #Metodo para trazer as colunas
    def info_colunas(self):
        return list(self.dados[0].keys())
    #Metodo que renomeia as colunas
    def renomear (self, key_map):
        new_dados = []
        for old in self.dados:
            temp = {}

            for key, value in old.items():
                temp[key_map[key]] = value
            
            new_dados.append(temp)

        self.dados = new_dados
        self.nome_colunas = self.info_colunas()
    #MEtodo que informa o tamanho do arquivo
    def tamanho(self):
        return len(self.dados)
    #Metodo que junta os arquivos
    def juntar (arq1, arq2):
        #Juntando as informacoes, ja lidando com a quantidade menor de colunas
        lista_combinada = []
        lista_combinada.extend(arq1.dados)
        lista_combinada.extend(arq2.dados)
        
        return Dado(lista_combinada, 'lista')
    #Metodo que tranforma os dados da tabela, adicionando valor ao campo que nao tem
    def tranformar_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for colu in self.nome_colunas:
                linha.append(row.get(colu, "Indisponivel"))
            
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela
    #Metodo que salva o arquivo
    def salvar(self, path):
        dados_ajustados = self.tranformar_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_ajustados) 