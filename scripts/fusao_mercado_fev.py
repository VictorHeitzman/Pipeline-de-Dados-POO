from processamento_dados import Dados

#   Variaveis de caminho
path_json          = r'data_raw/dados_empresaA.json'
path_csv           = r'data_processed\dados_empresaB.csv'
path_gravado       = r'data_processed/dados_combinados.csv'

#   cabecalhos antigos para os novos
key_mapping = {'Nome do Item': 'Nome do Produto',
                'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB = Dados(path_csv)
dados_empresaA = Dados(path_json)

dados_empresaB.renomeia_cabecalho(key_mapping)

dados_fusao = Dados.concatena_dados(dados_empresaA, dados_empresaB)

dados_fusao.grava_dados(path_gravado)
print(dados_fusao.dados)
