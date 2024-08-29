import json
import csv

class Dados:
    def __init__(self, path) -> None:
        self.path       = path
        self.dados      = self.leitura_dados()
        self.coluna     = self.retorna_cabecalho()

    def leitura_dados(self):
        if 'csv' in self.path:
            dados = self.leitura_csv()

        elif 'json' in self.path:
            dados = self.leitura_json()

        else:
            dados = self.path
            self.path = 'lista em memoria'
        
        return dados

    
    def leitura_json(self):
        dados_json = []    
        with open (self.path, 'r') as arquivo:
            dados_json = json.load(arquivo)
        return dados_json

    def leitura_csv(self):    
        dados_csv = []
        with open(self.path, 'r') as arquivo_csv:
            spamreader = csv.DictReader(arquivo_csv, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv
    
    def retorna_cabecalho(self):
        return list(self.dados[-1].keys()) 

    def renomeia_cabecalho(self, key_mapping):
        new_dados_csv = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados_csv.append(dict_temp)
        
        self.dados      = new_dados_csv
        self.coluna     = self.retorna_cabecalho()

    def concatena_dados(dadosA, dadosB):
        combine_list = []
        combine_list.extend(dadosA.dados)
        combine_list.extend(dadosB.dados)
        return Dados(combine_list)

    def transforma_tabela(self):
        dados_combinados_tabela = [self.coluna]

        for row in self.dados:
            linha = []
            for coluna in self.coluna:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela

    def grava_dados(self, path):

        dados_combinados_tabela = self.transforma_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
