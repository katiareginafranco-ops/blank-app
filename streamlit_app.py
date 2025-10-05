import streamlit as st
import pandas as pd
import numpy as np
pip list

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

st.set_page_config(page_title="Análise ENEM ES 2024", layout="wide")

st.title("📚 Análise da Redação - ENEM ES 2024")

# Função para carregar os dados com cache
@st.cache_data
def carregar_dados(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

# Upload do arquivo
uploaded_file = st.file_uploader("Carregue o arquivo ENEM_ES_2024_REDAÇÃO.csv", type="csv")

if uploaded_file:
    df = carregar_dados(uploaded_file)
    st.success("Arquivo carregado com sucesso!")

    # Visualização inicial
    if st.checkbox("👀 Visualizar primeiras linhas da tabela"):
        st.write(df.head())

    # Sidebar para filtros
    st.sidebar.header("🔍 Filtros")
    municipios = sorted(df['NOME MUN. PROVA'].dropna().unique())
    status_redacao = sorted(df['STATUS REDAÇÃO'].dropna().unique())
    tipos_escola = sorted(df['DEP. ADMIN.'].dropna().unique())

    municipio_filtro = st.sidebar.multiselect("Filtrar por Município", municipios, default=municipios)
    status_filtro = st.sidebar.multiselect("Filtrar por Status da Redação", status_redacao, default=status_redacao)
    escola_filtro = st.sidebar.multiselect("Filtrar por Tipo de Escola", tipos_escola, default=tipos_escola)

    df_filtrado = df[
        (df['NOME MUN. PROVA'].isin(municipio_filtro)) &
        (df['STATUS REDAÇÃO'].isin(status_filtro)) &
        (df['DEP. ADMIN.'].isin(escola_filtro))
    ]

    st.markdown("## 📍 Incidência do Status da Redação por Município")
    incidencia = df_filtrado.groupby(['NOME MUN. PROVA', 'STATUS REDAÇÃO']).size().unstack(fill_value=0)

    fig1, ax1 = plt.subplots(figsize=(12, 6))
    incidencia.plot(kind='bar', stacked=True, ax=ax1)
    ax1.set_title("Incidência do Status da Redação por Município")
    ax1.set_xlabel("Município")
    ax3.set_ylabel("Quantidade")
    ax3.legend(title="Status", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig3)

    st.markdown("## 📄 Exibição da Tabela Completa Filtrada")
    st.dataframe(df_filtrado)

else:
    st.info("Por favor, carregue o arquivo CSV para iniciar a análise.")
