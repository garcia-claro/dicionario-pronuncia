import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dicionário de Pronúncias", page_icon="🗣️")

st.title("🗣️ Consulta de Pronúncia")
st.markdown("Digite a palavra abaixo para saber como pronunciá-la.")

# Carregar a base de dados
try:
    df = pd.read_excel("dados.xlsx")
    
    # Criar a caixa de busca
    busca = st.text_input("Palavra desejada:").strip().lower()

    if busca:
        # Procura na coluna 'palavra' ignorando maiúsculas/minúsculas
        resultado = df[df['palavra'].str.lower() == busca]
        
        if not resultado.empty:
            pronuncia_final = resultado.iloc[0]['pronuncia']
            st.success(f"A pronúncia de **{busca.capitalize()}** é:")
            st.header(f"👉 {pronuncia_final}")
        else:
            st.warning("Ops! Essa palavra não foi encontrada no banco de dados.")

except Exception as e:
    st.error("Erro: Certifique-se de que o arquivo 'dados.xlsx' está na mesma pasta que este programa.")