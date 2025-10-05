import streamlit as st

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

import streamlit as st
import pandas as pd

# --- Configurações Iniciais e Título ---
st.set_page_config(
    page_title="Análise Descritiva de Dados do ENEM",
    layout="wide"
)

st.title('📊 Análise Descritiva Interativa do ENEM')
st.markdown('---')

# Função para carregar dados de forma eficiente (cache)
# Isso evita recarregar o arquivo toda vez que o Streamlit interage
@st.cache_data
def load_data(uploaded_file):
    """Lê o arquivo CSV e retorna um DataFrame do Pandas."""
    # Tenta ler com diferentes separadores e encodings, comum em arquivos brasileiros
    try:
        # Tentativa comum para arquivos brasileiros (separador ';')
        df = pd.read_csv(uploaded_file, sep=';', encoding='latin1', low_memory=False)
    except Exception:
        # Tentativa padrão (separador ',' e encoding 'utf-8')
        uploaded_file.seek(0) # Volta ao início do arquivo se a primeira leitura falhou
        df = pd.read_csv(uploaded_file, encoding='utf-8', low_memory=False)
    
    return df

# --- Upload do Arquivo ---
uploaded_file = st.file_uploader(
    "📤 Escolha o arquivo CSV do ENEM (ex: ENEM_ES_2024.csv)",
    type="csv"
)

if uploaded_file is not None:
    # Carregando os dados
    df = load_data(uploaded_file)
    st.success(f'Arquivo carregado com sucesso! Total de linhas: {len(df):,}')

    st.markdown('---')

    # 1. Tabela Descritiva (Pandas describe())
    st.header('1. Tabela Descritiva dos Dados Numéricos')
    st.info('Usamos `df.describe().T` para gerar as estatísticas das colunas numéricas (Média, Desvio Padrão, Mínimo, Máximo, Quartis).')
    
    try:
        # Transpõe (.T) o describe para que as estatísticas fiquem nas colunas e as variáveis nas linhas
        # Formata os números para duas casas decimais
        st.dataframe(
            df.describe().T.style.format("{:.2f}"),
            use_container_width=True
        )
    except Exception as e:
        st.error(f"Não foi possível gerar as estatísticas descritivas. Verifique a estrutura do seu CSV. Erro: {e}")
        st.dataframe(df.head()) # Mostra o cabeçalho para debug

    st.markdown('---')

    # 2. Gráfico de Barras (st.bar_chart)
    # Exemplo: Comparação da Média da Nota de Redação por Gênero
    st.header('2. Gráfico de Barras com st.bar_chart')
    st.subheader('Média da Nota de Redação por Gênero (Exemplo)')
    st.write('Para o gráfico, calculamos a média da coluna **NU_NOTA_REDACAO** agrupada pela coluna **TP_SEXO**.')

    # Colunas comuns no ENEM para este exemplo
    GENDER_COL = 'TP_SEXO'
    SCORE_COL = 'NU_NOTA_REDACAO'
    
    # Verifica se as colunas necessárias existem na base
    if GENDER_COL in df.columns and SCORE_COL in df.columns:
        
        # Filtra para remover valores nulos ou inválidos na coluna da nota
        df_filtered = df.dropna(subset=[SCORE_COL])
        
        # Agregação: Calcula a média da nota de redação por gênero
        chart_data = df_filtered.groupby(GENDER_COL)[SCORE_COL].mean().reset_index()
        
        # Renomeia as colunas para melhor clareza no gráfico
        chart_data.columns = ['Gênero', 'Média da Redação'] 
        
        # Exibe o gráfico de barras
        st.bar_chart(
            chart_data, 
            x='Gênero', 
            y='Média da Redação', 
            color="#279930" # Cor verde para destaque
        )
        
        st.caption('Tabela de dados usada para o gráfico:')
        st.dataframe(chart_data)

    else:
        st.warning(f"As colunas essenciais ('{GENDER_COL}' ou '{SCORE_COL}') não foram encontradas no seu arquivo para gerar o gráfico. Por favor, ajuste o código para usar colunas existentes.")
        
else:
    st.info("⚠️ Por favor, faça o upload do seu arquivo CSV para começar a análise.")
