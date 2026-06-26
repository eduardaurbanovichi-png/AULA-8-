 # EXERCICIO 4


# faça:

# Contexto

# Em uma análise de textos, palavras como “de”, “a”, “o”, 
# “para” não ajudam na interpretação
#  e precisam ser removidas para melhorar a análise.

# Objetivo

# Remova stopwords de um texto em português.

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
from nltk.corpus import stopwords

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Título
st.title("Exercício 4 - Remoção de Stopwords")

# Texto de entrada
texto = st.text_area(
    "Digite um texto:",
    "O aluno foi para a escola e fez a atividade com o professor."
)

# Botão
if st.button("Analisar", key="ex4"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Stopwords em português
    stop_words = set(stopwords.words('portuguese'))

    # Remove stopwords
    tokens_filtrados = [t for t in tokens if t.isalpha() and t not in stop_words]

    # Resultado
    st.write("### Texto original (tokens):")
    st.write(tokens)

    st.write("### Texto sem stopwords:")
    st.write(tokens_filtrados)