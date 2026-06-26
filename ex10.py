 # EXERCICIO 10


# faça:

# Contexto

# Uma empresa quer entender o conteúdo de avaliações de 
# produtos para identificar se os clientes
#  estão satisfeitos ou insatisfeitos sem leitura manual.

# Objetivo

# Combine tokenização + 
# condicional para analisar sentimento básico de um texto

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
from nltk.sentiment import SentimentIntensityAnalyzer

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('vader_lexicon', quiet=True)

# Título
st.title("Exercício 10 - Análise de Sentimento com NLP")

# Entrada do usuário
texto = st.text_area(
    "Digite uma avaliação de produto:",
    "O produto é ótimo, mas o atendimento foi ruim."
)

# Botão
if st.button("Analisar", key="ex10"):

    # -----------------------
    # TOKENIZAÇÃO
    # -----------------------
    tokens = word_tokenize(texto.lower())

    # -----------------------
    # ANÁLISE DE SENTIMENTO
    # -----------------------
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(texto)

    compound = scores["compound"]

    # Classificação por regra
    if compound >= 0.05:
        label = "Satisfeito 😊"
    elif compound <= -0.05:
        label = "Insatisfeito 😡"
    else:
        label = "Neutro 😐"

    # -----------------------
    # RESULTADO
    # -----------------------
    st.write("### Resultado da análise")
    st.write("Texto analisado:", texto)
    st.write("Tokens:", tokens)
    st.write("Label:", label)
    st.write("Score:", compound)

    
