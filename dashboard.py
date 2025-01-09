import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

st.title("Dashboard Operacional")

# Caminho para o arquivo base de dados consolidado
file_path = "Base de dados Resumo_Operacional_Com_Graficos.xlsx"

# Verifica se o arquivo existe
if os.path.exists(file_path):
    # Lê todas as abas do Excel
    sheets = pd.read_excel(file_path, sheet_name=None)

    # Seleção de abas
    sheet_names = list(sheets.keys())
    selected_sheet = st.selectbox("Selecione a aba que deseja visualizar:", sheet_names)

    # Carrega os dados da aba selecionada
    df = sheets[selected_sheet]

    # Formatação de valores como moeda
    columns_to_format = ['Vlr Médio Transporte', 'Lucro Bruto', 'Saldo Mensal', 'Custo Total']
    for col in columns_to_format:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: f"R$ {x:,.2f}" if pd.notnull(x) else x)

    # Exibe os dados na tabela
    st.subheader(f"Dados Consolidados - Aba: {selected_sheet}")
    st.dataframe(df)

    # Gráfico de Sacas Entregues por Mês
    st.subheader("Gráfico de Sacas Entregues por Mês")
    if 'Mês' in df.columns and 'Sacas Entregues' in df.columns:
        fig, ax = plt.subplots()
        df.plot(x='Mês', y='Sacas Entregues', kind='bar', ax=ax, legend=False)
        ax.set_title("Sacas Entregues por Mês")
        ax.set_ylabel("Sacas Entregues")
        ax.set_xlabel("Mês")
        st.pyplot(fig)
else:
    st.error("O arquivo base de dados consolidado não foi encontrado no repositório.")
