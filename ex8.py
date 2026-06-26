 # EXERCICIO 8


# faça:

# Contexto

# Uma empresa quer classificar mensagens automaticamente em
#  “suporte técnico” 
# ou “financeiro” com base em palavras específicas.

# Objetivo

# Crie regras condicionais simples para classificar mensagens.

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
st.title("Exercício 8 - Classificação de Mensagens")

# Palavras-chave por categoria
suporte_tecnico = ["erro", "bug", "falha", "problema", "sistema", "travou"]
financeiro = ["pagamento", "boleto", "cobrança", "cartão", "fatura", "cobrar"]

# Entrada do usuário
texto = st.text_area(
    "Digite sua mensagem:",
    "Estou com erro no sistema e não consigo pagar o boleto."
)

# Botão
if st.button("Analisar", key="ex8"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Categoria padrão
    categoria = "Indefinido"

    # Regras condicionais
    if any(p in tokens for p in suporte_tecnico):
        categoria = "Suporte Técnico 🖥️"
    elif any(p in tokens for p in financeiro):
        categoria = "Financeiro 💰"

    # Resultado
    st.write("### Categoria identificada:")
    st.write(categoria)

    st.write("### Tokens:")
    st.write(tokens)
