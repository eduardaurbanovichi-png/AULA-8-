




# EXERCICIO 1


# faça:

# Contexto

# Uma empresa recebe centenas de mensagens de clientes 
# todos os dias

# Objetivo

# Ela precisa separar automaticamente o texto em 
# palavras para facilitar a análise e organização das 
# informações.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Audiência

# Iniciante em NLP que quer ver o básico funcionando.

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



# Baixa o recurso necessário para tokenização
nltk.download('punkt', quiet=True)

# Título da aplicação
st.title("Exercício 1 - Simulador de Análise de Sentimento com Tokenização")

# Lista simples de palavras para simular sentimento
palavras_positivas = ["bom", "ótimo", "excelente", "feliz", "incrível", "bom"]
palavras_negativas = ["ruim", "péssimo", "horrível", "triste", "lento", "fraco"]

# Entrada do usuário
texto = st.text_area(
    "Digite um texto:",
    "O serviço foi ruim, mas o atendimento foi bom."
)

# Botão para analisar
if st.button("Analisar", key="ex1"):

    # Tokenização (separar em palavras)
    tokens = word_tokenize(texto.lower())

    # Contadores simples
    positivos = 0
    negativos = 0

    # Análise palavra por palavra
    for palavra in tokens:
        if palavra in palavras_positivas:
            positivos += 1
        elif palavra in palavras_negativas:
            negativos += 1

    # Decisão final
    if positivos > negativos:
        resultado = "Sentimento Positivo 😊"
    elif negativos > positivos:
        resultado = "Sentimento Negativo 😡"
    else:
        resultado = "Sentimento Neutro 😐"

    # Resultados na tela
    st.subheader("Resultado da Análise")
    st.write(resultado)

    st.write("### Tokens encontrados:")
    st.write(tokens)

    st.write("### Contagem:")
    st.write(f"Positivos: {positivos}")
    st.write(f"Negativos: {negativos}")




       

    

    

         