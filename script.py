# Importações de bibliotecas necessárias para funcionalidades do script
from typing import Text
import streamlit as st  # Biblioteca para criar interfaces web interativas
import io  # Manipulação de arquivos em memória
import base64  # Codificação e decodificação de base64
import pandas as pd  # Manipulação de dados tabulares
import numpy as np  # Operações numéricas e matrizes
from datetime import date, datetime, time  # Manipulação de datas e horários
import re  # Operações com expressões regulares
import unicodedata  # Tratamento de caracteres Unicode
import xlsxwriter  # Criação de arquivos Excel
import openpyxl  # Leitura e manipulação de arquivos Excel
import os  # Operações com o sistema operacional
from converter import excel_csv, csv_excel  # Funções personalizadas para conversão entre Excel e CSV
from function import up, lower, remover_caracteres_especiais, aplicar_regex_df  # Funções utilitárias personalizadas
from b2b import b2b  # Função personalizada para Conexia B2B
from b2c import b2c  # Função personalizada para Conexia B2C
from seb import seb  # Função personalizada para SEB
from premium import premium  # Função personalizada para Premium
from pedido_programado import pedido_programado  # Função personalizada para pedidos programados

# ============================================================================================================================
# Função de autenticação de senha
def check_password():
    """Verifica se o usuário inseriu a senha correta."""
    def password_entered():
        """Verifica a senha digitada pelo usuário."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True  # Marca como senha correta
            del st.session_state["password"]  # Remove a senha da sessão por segurança
        else:
            st.session_state["password_correct"] = False  # Marca como senha incorreta

    if "password_correct" not in st.session_state:
        # Primeira execução: exibe campo para digitar senha
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Senha incorreta: exibe erro
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        # Senha correta
        return True

# ============================================================================================================================

# Se a senha for correta, executa o restante do script
if check_password():
    buffer = io.BytesIO()  # Buffer para operações de I/O

    # Configurações iniciais do Streamlit
    st.set_page_config(
        page_title="Script de soluções", 
        page_icon="⭐", 
        layout="wide", 
        initial_sidebar_state="expanded"
    )

    # Configuração da barra lateral
    st.sidebar.image('https://sso.lex.education/assets/images/new-lex-logo.png', width=100)
    st.sidebar.title('Script de solução - Simulador')

    # Opções de escolha na barra lateral
    page = [
        'CONEXIA B2B', 
        'CONEXIA B2C', 
        'SEB', 
        'PREMIUM', 
        'EXCEL PARA CSV', 
        'CSV PARA EXCEL', 
        'PEDIDO PROGRAMADO'
    ]
    choice = st.sidebar.selectbox('Selecione:', page)

# ============================================================================================================================

    # Funções utilitárias para manipulação de dados
    def up(data):
        """Converte os nomes das colunas e valores de strings para maiúsculas."""
        data.columns = data.columns.str.upper()
        for columns in data.columns:
            if data[columns].dtype == 'object':
                data[columns] = data[columns].str.upper()
        return data

    def lower(data):
        """Converte os nomes das colunas e valores de strings para minúsculas."""
        data.columns = data.columns.str.lower()
        for columns in data.columns:
            data[columns] = data[columns].str.lower()
        return data

    def remover_caracteres_especiais(texto):
        """Remove caracteres especiais de uma string."""
        texto_sem_especiais = re.sub(r'[^\w\s]', '', texto)
        return texto_sem_especiais
    
    def aplicar_regex_df(df, padrao, substituicao=''):
        """Aplica uma regex a todas as colunas de um DataFrame."""
        regex = re.compile(padrao)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: regex.sub(substituicao, x) if isinstance(x, str) else x)

    def processar_excel(sheet_name):
        """Processa um arquivo Excel enviado pelo usuário."""
        file = st.file_uploader("Selecione um arquivo Excel", type=["xlsx"])
    
        if file is not None:
            simul = pd.read_excel(file, sheet_name=sheet_name)
            simul = simul.assign(Bimestre="ANUAL")  # Adiciona coluna fixa
            simul.replace(0, np.nan, inplace=True)  # Substitui 0 por NaN
            up(simul)  # Aplica a função 'up'
            return simul
        return None  # Retorna None se nenhum arquivo for enviado

# ============================================================================================================================

    # Chama a função correspondente à escolha feita na barra lateral
    if choice == 'B2B':
        b2b()

    if choice == 'B2C':
        b2c()

    if choice == 'ESCOLA':
        seb()
    
    if choice == 'PREMIUM':
        premium()

    if choice == 'EXCEL PARA CSV':
        excel_csv()

    if choice == 'CSV PARA EXCEL':
        csv_excel()
    
    if choice == 'PEDIDO PROGRAMADO':
        pedido_programado()










