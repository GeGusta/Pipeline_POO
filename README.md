# Pipeline_POO
O prejeto tem como objetivo criar uma Pipeline de Dados utilizando Python Orientado a Objetos. Foi informado uma situação de negócio e utilizando Python, foi proposto scripts para tratamento dos dados.

## Objetivo
A Empresa A e Empresa B fundiram e querem saber o resultado após essa fusão. Cada uma disponibilizou um arquivo em com as informações de vendas e foi solicitado para juntar essas duas informações e disponibilizar em um arquivo .csv para o time realizar as análises.
O arquivo da Empresa A é um JSON e o da Empresa B um CSV.

## Método
Foi feita uma exploração inicial nos arquivos para saber como as informações estavam e que tratamento era necessário. **Isso está disponível no arquivo 'notebooks/exploracao.ipynb'**.
### Questionamentos que surgiram
- Os arquivos estão em formatos diferentes, um em JSON e outro em CSV;
- O nome das colunas são diferentes nos arquivos;
- Tem uma coluna a menos no arquivo da empresa A.
### Tratamento
Para cada tipo de arquivo foi feito um método diferente de leitura para resultar em aquivos com listas de dicionários para ambos.
Ex: JSON
  {'Nome do Produto': 'Blush em pó',
  'Categoria do Produto': 'Eletrodomésticos',
  'Preço do Produto (R$)': 79.41,
  'Quantidade em Estoque': 7,
  'Filial': 'Filial 7'},
  CSV
  {'Nome do Item': 'Lápis de sobrancelha',
  'Classificação do Produto': 'Roupas',
  'Valor em Reais (R$)': '55.17',
  'Quantidade em Estoque': '62',
  'Nome da Loja': 'Filial 1',
  'Data da Venda': '2023-04-13 18:58:06.794203'},
  
As colunas do arquivo da Empresa B foram renomeadas pelo seguinte key_map, informando a coluna antiga e sua correspondente nova.
key_map = {'Nome do Item':'Nome do Produto', 
           'Classificação do Produto':'Categoria do Produto', 
           'Valor em Reais (R$)': 'Preço do Produto (R$)',
           'Quantidade em Estoque': 'Quantidade em Estoque',
           'Nome da Loja':'Filial',
           'Data da Venda':'Data da Venda'
           }
Para a coluna faltante no arquivo da Empresa A, "Data da Venda", foi colocado como valor "Indisponível" na junção dos dois arquivos.

## Resultado
Foram feitos 4 arquivos Python para tratamento deles. O resultado obtido é o mesmo, mas por métodos diferentes.
- script.py: é o tratamento que foi desenvolvido na exploração com o Notebook de forma sucinta e com indicação do que está sendo feito;
- script2.py: utiliza de funções para o tratamento dos dados;
- processamento_dados.py: Classe Dado desenvolvida para ter os atributos e métodos necessário para fazer o tratamento proposto;
- scriptPOO.py: Utiliza das classes para organizar o tratamento.

Esses Scripts fazem o seguinte fluxo:
1. Leem os arquivos JSON e CSV;
2. Renomeiam as colunas do arquivo da Empresa B
3. Juntam as informações;
4. Adicionam "Indisponível" no campo de 'Data da Venda" para os registros sem essa informação;
5. Salvam o arquivo resultante do processamento na pasta 'data processed'
