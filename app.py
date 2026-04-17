import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dicionário de Pronúncia", page_icon="🗣️")

st.title("🗣️ Consulta de Pronúncia")
st.write("Digite a palavra abaixo para saber como pronunciá-la.")

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    try:
        # Tenta ler o excel garantindo que use a biblioteca correta
        df = pd.read_excel("dados.xlsx", engine="openpyxl")
        # Remove espaços em branco extras nos nomes das colunas e nos textos
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

df = carregar_dados()

if df is not None:
    busca = st.text_input("Palavra desejada:").strip().lower()

    if busca:
        # Faz a busca ignorando maiúsculas/minúsculas
        resultado = df[df['Palavra'].str.lower().str.strip() == busca]
        
        if not resultado.empty:
            pronuncia = resultado.iloc[0]['Pronúncia']
            st.success(f"**Pronúncia:** {pronuncia}")
        else:
            st.warning("Palavra não encontrada no dicionário.")
