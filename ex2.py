# EXERCICIO 2


# faça:

# Contexto

# Um sistema de análise de dados precisa identificar quais palavras aparecem com mais frequência em 
# avaliações de clientes para entender padrões de comportamento.

# Objetivo

# Conte a frequência das palavras em um texto simples.

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
import pandas as pd

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Título
st.title("Exercício 2 - Análise de Frequência de Palavras")

# Entrada do usuário
texto = st.text_area(
    "Digite uma avaliação:",
    "O produto é bom, muito bom e o atendimento também é excelente e bom."
)

# Botão
if st.button("Analisar", key="ex2"):

    # ---------------------------
    # TOKENIZAÇÃO
    # ---------------------------
    tokens = word_tokenize(texto.lower())

    # Remove pontuação e números
    tokens_limpos = [t for t in tokens if t.isalpha()]

    # ---------------------------
    # STOPWORDS (NOVO)
    # ---------------------------
    stop_words = set(stopwords.words('portuguese'))
    tokens_filtrados = [t for t in tokens_limpos if t not in stop_words]

    # ---------------------------
    # FREQUÊNCIA
    # ---------------------------
    frequencia = Counter(tokens_filtrados)
    top_palavras = frequencia.most_common(5)

    # ---------------------------
    # RESULTADOS
    # ---------------------------
    st.subheader("📊 Resultados da Análise")

    st.write("**Total de palavras analisadas:**", len(tokens_filtrados))

    if top_palavras:
        palavra_mais_comum = top_palavras[0]
        st.write("**Palavra mais frequente:**", palavra_mais_comum)
    else:
        st.write("Nenhuma palavra relevante encontrada.")

    st.write("### Tokens processados:")
    st.write(tokens_filtrados)

    st.write("### Top palavras:")
    st.write(top_palavras)

    # ---------------------------
    # GRÁFICO (NOVO)
    # ---------------------------
    if top_palavras:
        df = pd.DataFrame(top_palavras, columns=["Palavra", "Frequência"])
        st.bar_chart(df.set_index("Palavra"))