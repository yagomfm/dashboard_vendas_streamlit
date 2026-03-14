import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.title('DADOS BRUTOS')

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format="%d/%m/%Y")

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))

st.sidebar.title('Filtros')
with st.sidebar.expander('Nome do produto'):
    produtos = st.multiselect('Selecione os produtos', dados['Produto'].unique(), dados['Produto'].unique())
with st.sidebar.expander('Preço do produto'):
    preco = st.slider('Selecione o preço', 0, 5000, (0, 5000))
with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input('Selecione a data', (dados['Data da Compra'].min(), dados['Data da Compra'].max()))
with st.sidebar.expander('Categoria do produto'):
    categoria = st.multiselect('Selecione as categorias', dados['Categoria do Produto'].unique(), dados['Categoria do Produto'].unique())
with st.sidebar.expander('Preço do frete'):
    preco_frete = st.slider('Selecione o preço', 0, 250, (0, 250))
with st.sidebar.expander('Nome do vendedor'):
    vendedores = st.multiselect('Selecione o vendedor', dados['Vendedor'].unique(), dados['Vendedor'].unique())
with st.sidebar.expander('Local da compra'):
    local_compra = st.multiselect('Selecione o local', dados['Local da compra'].unique(), dados['Local da compra'].unique())
with st.sidebar.expander('Avaliação da compra'):
    avaliacao_compra = st.slider('Selecione a avaliação', 0, 5, (0,5))
with st.sidebar.expander('Tipo de pagamento'):
    tipo_pagamento = st.multiselect('Selecione o tipo de pagamento', dados['Tipo de pagamento'].unique(), dados['Tipo de pagamento'].unique())
with st.sidebar.expander('Quantidade de parcelas'):
    quantidade_parcelas = st.slider('Selecione a quantidade', 0, 24, (0,24))

query = '''
    Produto in @produtos and \
    @preco[0] <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1] and \
    `Categoria do Produto` in @categoria and \
    @preco_frete[0] <= Frete <= @preco_frete[1] and \
    Vendedor in @vendedores and \
    `Local da compra` in @local_compra and \
    @avaliacao_compra[0] <= `Avaliação da compra` <= @avaliacao_compra[1] and \
    `Tipo de pagamento` in @tipo_pagamento and \
    @quantidade_parcelas[0] <= `Quantidade de parcelas` <= @quantidade_parcelas[1]
'''

dados_filtrados = dados.query(query)
dados_filtrados = dados_filtrados[colunas]

st.dataframe(dados_filtrados)

st.markdown(f'A tabela possui :blue[{dados_filtrados.shape[0]}] linhas e :blue[{dados_filtrados.shape[1]}] colunas.')