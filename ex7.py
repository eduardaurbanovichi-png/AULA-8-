# EXERCICIO 7


# faça:

# Contexto

# Um analista quer saber quais palavras mais aparecem 
# em reclamações de clientes para melhorar o produto.

# Objetivo

# Crie um código que identifique 
# as palavras mais frequentes em um texto de reclamação.

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
from collections import Counter

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Título
st.title("Exercício 7 - Frequência em Reclamações")

# Texto de entrada
texto = st.text_area(
    "Digite uma reclamação:",
    "O produto é ruim, ruim mesmo, e o atendimento foi péssimo e lento."
)

# Botão
if st.button("Analisar", key="ex7"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Remove pontuação
    tokens = [t for t in tokens if t.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('portuguese'))
    tokens_filtrados = [t for t in tokens if t not in stop_words]

    # Frequência
    frequencia = Counter(tokens_filtrados)

    # Top palavras
    top_palavras = frequencia.most_common(5)

    # Resultado
    st.write("### Palavras mais frequentes:")
    st.write(top_palavras)

    st.write("### Tokens limpos:")
    st.write(tokens_filtrados)
