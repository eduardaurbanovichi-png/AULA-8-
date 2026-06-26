# EXERCICIO 5


# faça:

# Contexto

# Uma equipe de marketing quer entender rapidamente se 
# comentários de clientes
# são positivos ou negativos com base em palavras-chave

# Objetivo

# Crie um sistema simples de classificação de sentimento usando condicionais.

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
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)

st.title("Exercício 5 - Análise de Sentimento Dinâmica")

# Entrada livre do usuário
texto = st.text_area("Digite qualquer frase ou comentário:")

if st.button("Analisar", key="ex5"):

    # Proteção contra texto vazio
    if texto.strip() == "":
        st.warning("Digite algum texto para análise.")
    else:

        sia = SentimentIntensityAnalyzer()
        scores = sia.polarity_scores(texto)

        compound = scores["compound"]

        # Classificação
        if compound >= 0.05:
            label = "Positivo 😊"
        elif compound <= -0.05:
            label = "Negativo 😡"
        else:
            label = "Neutro 😐"

        # Resultado
        st.write("### Resultado da análise")
        st.write("Texto analisado:", texto)
        st.write("Label:", label)
        st.write("Score:", compound)