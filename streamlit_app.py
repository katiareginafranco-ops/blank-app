import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Análise das Causas de Nota Zero na Redação do ENEM 2024",
    layout="wide"
)

# Exibe o título da página
st.title("Análise das Causas de Nota Zero na Redação do ENEM 2024")

# Exibe o nome do autor logo abaixo, usando markdown para itálico
st.markdown("_Por: Kátia Regina Franco_")

# Exemplo de colunas
coluna1, coluna2 = st.columns((2, 1))
with coluna1:

    # ---- Título e Introdução da Página Inicial ----
    st.title("📊 Desvendando a Redação ENEM 2024: Por que a Nota Zero?")
    st.markdown("""
        Bem-vindo ao protótipo de análise das redações do ENEM 2024.
        Aqui, você pode explorar e entender os principais motivos que levam as
        redações a receberem a nota zero, uma situação que pode ser evitada com
        informação e estudo.
    
        Neste aplicativo, vamos desmistificar os critérios de anulação para ajudar
        estudantes e educadores a se prepararem melhor. Embora o recorte se dá nos resultados do estado do Espírito Santo, estudantes de outros estados também podem utilizar as informações e dicas.
    """)
st.markdown("---")
with coluna2: 
    with st.container(border=True):
     # Lista dos cards com título, ícone e conteúdo
        cards = [
        {
            "titulo": "1. Fuga total ao tema",
            "tipo": "error",
            "icone": "🚨",
            "conteudo": """
            A redação deve abordar o tema proposto pelo ENEM. Se o texto foge completamente do
            assunto, o participante recebe nota zero.
            """
        },
        {
            "titulo": "2. Cópia dos textos motivadores",
            "tipo": "warning",
            "icone": "📄",
            "conteudo": """
            Copiar trechos dos textos de apoio (os chamados "textos motivadores")
            também anula a redação. O texto deve ser autoral, usando os textos motivadores
            apenas como referência.
            """
        },
        {
            "titulo": "3. Anulada - Desenhos ou impropérios",
            "tipo": "info",
            "icone": "✍️",
            "conteudo": """
            Qualquer tipo de desenho, anotação indevida ou ofensa no espaço da redação, nome, assinatura, pode
            levar à anulação, já que pode ser um tipo de código para identificar o participante.
            """
        },
        {
            "titulo": "4. Desrespeito aos Direitos Humanos",
            "tipo": "success",
            "icone": "⚖️",
            "conteudo": """
            A proposta de intervenção, que é um dos critérios de avaliação, não pode
            violentar os direitos humanos.
            """
        },
        {
            "titulo": "5. Não atendimento ao tipo textual",
            "tipo": "error",
            "icone": "📚",
            "conteudo": """
            O texto precisa ser um "dissertativo-argumentativo". Qualquer outra forma,
            como poema, narração, ou receita, resulta em nota zero.
            """
        },
        {
            "titulo": "6. Texto com até 7 linhas",
            "tipo": "warning",
            "icone": "📏",
            "conteudo": """
            A redação deve ter, no mínimo, 8 linhas escritas.
            """
        },
        {
            "titulo": "7. Texto com Parte desconectada",
            "tipo": "info",
            "icone": "🔗",
            "conteudo": """
            A redação contém trechos sem relação com o tema proposto ou com o projeto de texto do candidato, atentando contra a seriedade da prova, tais como hino de time de futebol ou receita culinária.
            """
        },
        {
            "titulo": "8. Folha de redação em branco",
            "tipo": "success",
            "icone": "📄",
            "conteudo": """
            A folha de redação não contém texto algum escrito.
            """
        },
    ]

    # Mostra um dropdown para selecionar um card
        st.subheader("Escolha um dos motivos de Nota Zero:")
        opcao = st.selectbox(
        "",
        [f"{card['titulo']}" for card in cards]
    )

    # Filtra o card selecionado
        card_selecionado = next(card for card in cards if card["titulo"] == opcao)

        # Exibe o card com o tipo de mensagem correto
        tipo = card_selecionado["tipo"]
        texto = card_selecionado["titulo"]
        icone = card_selecionado["icone"]
        conteudo = card_selecionado["conteudo"]

        if tipo == "error":
            st.error(f"{texto}", icon=icone)
        elif tipo == "warning":
            st.warning(f"{texto}", icon=icone)
        elif tipo == "info":
            st.info(f"{texto}", icon=icone)
        elif tipo == "success":
            st.success(f"{texto}", icon=icone)

        st.markdown(conteudo)

# ---- Seção "Sobre e Fontes" ----
st.subheader("Sobre este Projeto e Fontes de Dados")
st.markdown("""
    Este é um projeto acadêmico da disciplina *Cloud Computing para produtos de dados*, do curso de pós-graduação **Mineração de Dados Educacionais**.
    O objetivo é usar dados abertos para gerar insights e ferramentas úteis.
   
    **Fonte de Dados:**
    Os dados utilizados para a futura expansão do aplicativo virão dos
    **Microdados do ENEM**, disponibilizados anualmente pelo **INEP**.
""")
st.markdown("---")

# carregar dataset
import streamlit as st
import pandas as pd

# Título do app
st.title("Análise da Redação - ENEM ES 2024")

# Upload do arquivo CSV
arquivo = st.file_uploader("Carregue o arquivo ENEM_ES_2024_REDAÇÃO.csv", type=["csv"])

# Verifica se o arquivo foi carregado
if arquivo is not None:
    # Lê o CSV em um DataFrame
    df = pd.read_csv(arquivo)

    # Exibe os dados
    st.subheader("Prévia dos Dados")
    st.write(df.head())

    # Informações básicas
    st.subheader("Informações Gerais")
    st.write(df.describe())
else:
    st.info("Por favor, carregue o arquivo CSV.")

