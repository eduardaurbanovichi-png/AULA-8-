 # EXERCICIO 3


# faça:

# Contexto

# Uma empresa de atendimento quer detectar automaticamente
#  mensagens com palavras negativas
#  para priorizar o suporte ao cliente.

# Objetivo

# Crie uma regra condicional para 
# identificar palavras como “ruim”, “péssimo” ou “erro”.

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

# Baixa recurso de tokenização
nltk.download('punkt', quiet=True)

# Título
st.title("Exercício 3 - Detecção de Mensagens Negativas")

# Lista de palavras negativas
palavras_negativas = ["ruim", "péssimo", "horrível", "erro", "falha", "problema"]

# Entrada do usuário
texto = st.text_area(
    "Digite uma mensagem do cliente:",
    "O sistema apresentou erro e o atendimento foi ruim."
)

# Botão
if st.button("Analisar", key="ex3"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Verificação de palavras negativas
    encontrados = []

    for palavra in tokens:
        if palavra in palavras_negativas:
            encontrados.append(palavra)

    # Decisão
    if len(encontrados) > 0:
        label = "⚠️ Mensagem NEGATIVA - Priorizar atendimento"
    else:
        label = "Mensagem Normal 👍"

    # Resultado
    st.write("### Resultado:")
    st.write(label)

    st.write("### Palavras negativas encontradas:")
    st.write(encontrados)

    st.write("### Tokens:")
    st.write(tokens)