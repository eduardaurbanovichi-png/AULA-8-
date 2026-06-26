  # EXERCICIO 6


# faça:

# Contexto

# Um chatbot precisa identificar palavras-chave dentro de uma
#  frase para direcionar o cliente para o setor correto.

# Objetivo

# Crie uma lógica que detecte palavras como “cancelar”,
#  “erro” e “pagamento”.

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
st.title("Exercício 6 - Chatbot por Palavras-chave")

# Palavras-chave por setor
cancelamento = ["cancelar", "cancelamento", "sair"]
erro = ["erro", "problema", "bug", "falha"]
pagamento = ["pagamento", "cobrança", "boleto", "cartão"]

# Entrada do usuário
texto = st.text_area(
    "Digite sua mensagem:",
    "Quero cancelar meu plano porque deu erro no pagamento."
)

# Botão
if st.button("Analisar", key="ex6"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Detectores
    setor = "Atendimento geral"

    if any(p in tokens for p in cancelamento):
        setor = "Setor de Cancelamento"
    elif any(p in tokens for p in erro):
        setor = "Suporte Técnico (Erros)"
    elif any(p in tokens for p in pagamento):
        setor = "Financeiro / Pagamentos"

    # Resultado
    st.write("### Resultado:")
    st.write("Setor identificado:", setor)

    st.write("### Tokens:")
    st.write(tokens)
