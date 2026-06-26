 # EXERCICIO 9


# faça:

# Contexto

# Um sistema de IA precisa limpar textos removendo pontuação
#  e deixando apenas palavras relevantes para análise.

# Objetivo

# Remova pontuação e normalize um texto (letras minúsculas).

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 


import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download necessário
nltk.download('punkt', quiet=True)

# Título
st.title("Exercício 9 - Limpeza e Normalização de Texto")

# Entrada do usuário
texto = st.text_area(
    "Digite um texto:",
    "O Produto é BOM!!!, mas o Atendimento foi RUIM..."
)

# Botão
if st.button("Analisar", key="ex9"):

    # Normalização (minúsculas)
    texto_normalizado = texto.lower()

    # Tokenização
    tokens = word_tokenize(texto_normalizado)

    # Remove pontuação e caracteres não alfabéticos
    tokens_limpos = [t for t in tokens if t.isalpha()]

    # Resultado
    st.write("### Texto original:")
    st.write(texto)

    st.write("### Tokens limpos:")
    st.write(tokens_limpos)
