import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# 📝 Apresentação da seção de análise
st.markdown("""
## ✍️ Análise dos Status da Redação

Nesta seção, você pode analisar como as redações foram avaliadas pela banca.  
Cada tipo de status — como *em branco*, *anulada*, *válida*, entre outros — é representado por um número específico, descrito na tabela abaixo.  

Essas informações ajudam a entender a distribuição dos participantes por status da redação, considerando **município** e **tipo de escola**.

---

### 🗂️ Tabela de Códigos de Status da Redação

| Código | Descrição                           |
|--------|-------------------------------------|
| 1      | Sem problemas                       |
| 2      | Anulada                             |
| 3      | Cópia do texto motivador            |
| 4      | Em branco                           |
| 6      | Fuga ao tema                        |
| 7      | Não atendimento ao tipo textual     |
| 8      | Texto insuficiente                  |
| 9      | Parte desconectada                  |

---
""")
st.markdown("---")

# Configuração da página
st.set_page_config(layout="wide", page_title="Análise ENEM Redação")
st.title("📊 Análise de Dados do ENEM")
st.markdown("---")

# Função para carregar os dados com cache
# Usamos st.cache_data para evitar recarregar o arquivo sempre que a página for alterada
@st.cache_data
def carregar_dados(uploaded_file):
    """Carrega o arquivo CSV em um DataFrame do Pandas."""
    try:
        # Tenta ler o arquivo
        df = pd.read_csv(uploaded_file, sep=',', encoding='utf-8')
        # Limpa nomes de colunas (opcional, mas boa prática)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo. Certifique-se de que é um CSV válido. Detalhe: {e}")
        return pd.DataFrame()

# Upload do arquivo
uploaded_file = st.file_uploader("📥ENEM_ES_2024_REDAÇÃO.csv", type=["csv"])

df = pd.DataFrame()
df_filtrado = pd.DataFrame()
if uploaded_file is not None:
    df = carregar_dados(uploaded_file)
    
    if not df.empty:
        st.success("Arquivo carregado com sucesso! Utilize a barra lateral para aplicar os filtros.")

        # 🔎 Visualização inicial
        if st.checkbox("👀 Visualizar primeiras linhas da tabela"):
            st.subheader("Primeiras 5 Linhas")
            st.dataframe(df.head())

        # 🎛️ Sidebar para filtros
        st.sidebar.header("🔍 Configuração de Filtros")

        # Garante que as colunas existem antes de tentar acessar
        try:
            municipios = sorted(df['NOME MUN. PROVA'].dropna().unique())
            status_redacao = sorted(df['STATUS REDAÇÃO'].dropna().unique())
            tipos_escola = sorted(df['DEP. ADMIN.'].dropna().unique())
        except KeyError as e:
            st.error(f"Erro: Coluna {e} não encontrada no arquivo. Verifique se o cabeçalho está correto.")
            st.stop()
            
        # Controles Multiselect
        municipio_filtro = st.sidebar.multiselect("Filtrar por Município", municipios, default=municipios)
        status_filtro = st.sidebar.multiselect("Filtrar por Status da Redação", status_redacao, default=status_redacao)
        escola_filtro = st.sidebar.multiselect("Filtrar por Tipo de Escola", tipos_escola, default=tipos_escola)

        # 🧹 Aplicando os filtros
        df_filtrado = df[
            (df['NOME MUN. PROVA'].isin(municipio_filtro)) &
            (df['STATUS REDAÇÃO'].isin(status_filtro)) &
            (df['DEP. ADMIN.'].isin(escola_filtro))
        ]

        # Resultados dos Filtros (Usa df_filtrado)
        st.markdown("---")
        st.subheader(f"Resultados Filtrados ({len(df_filtrado)} registros)")

        if df_filtrado.empty:
            st.warning("Nenhum dado corresponde aos filtros selecionados.")
        else:
            # 1. Estatísticas Rápidas
            st.markdown("##### Estatísticas da Redação")
            
             # Prepara os cálculos dos Status
            most_frequent_status, least_frequent_status, most_frequent_count, least_frequent_count = ('N/A', 'N/A', 0, 0)
            status_exists = 'STATUS REDAÇÃO' in df_filtrado.columns
            if status_exists:
                status_counts = df_filtrado['STATUS REDAÇÃO'].value_counts()
                if not status_counts.empty:
                    most_frequent_status = status_counts.index[0]
                    most_frequent_count = status_counts.iloc[0]
                    # Encontra o menos frequente de forma segura
                    if len(status_counts) > 1:
                        least_frequent_status = status_counts.index[-1]
                        least_frequent_count = status_counts.iloc[-1]
                    else:
                        # Se só houver um status, ele é o mais e menos frequente
                        least_frequent_status = most_frequent_status
            
            # Linha 1: Contagem e Status de Ocorrência
            col1, col2, col3 = st.columns(3)
            col1.metric("Total de Candidatos Filtrados", len(df_filtrado))
            
            # Métrica de maior ocorrência (Status)
            col2.metric("Status Redação de Maior Ocorrência", most_frequent_status, delta=f"{most_frequent_count} registros" if status_exists else None)
            
            # Métrica de menor ocorrência (Status)
            col3.metric("Status Redação de Menor Ocorrência", least_frequent_status, delta=f"{least_frequent_count} registros" if status_exists and len(status_counts) > 1 else None)
            st.markdown("---")
            
            # 2. Visualização da Tabela Filtrada
            st.markdown("## 📄 Exibição da Tabela Completa Filtrada")
            st.dataframe(df_filtrado, use_container_width=True)
            
            # 3. Download
            @st.cache_data
            def convert_df(df):
                # Converte o DataFrame para CSV para download
                return df.to_csv(index=False).encode('utf-8')

            csv = convert_df(df_filtrado)

            st.download_button(
                label="⬇️ Baixar Dados Filtrados (CSV)",
                data=csv,
                file_name='enem_dados_filtrados.csv',
                mime='text/csv',
            )
            
    else:
        st.warning("O DataFrame carregado está vazio. Verifique a estrutura do seu arquivo CSV.")

        st.markdown("---")

    # 2. Geração do Mapa de Calor (Distribuição de Status por Município)
            # df_mapa_status é necessário para o Heatmap e para o Gráfico de Barras Agrupadas (Seção 5)
    df_mapa_status = pd.DataFrame() # Inicializa fora do if para evitar erro de escopo no Bloco 5
    if status_exists and 'NOME MUN. PROVA' in df_filtrado.columns:
                st.markdown("---")
                st.subheader("🔥 Mapa de Calor: Distribuição do Status da Redação por Município")

                # Agrupando os dados filtrados para calcular a contagem de cada status por município
                df_mapa_status = df_filtrado.groupby(['NOME MUN. PROVA', 'STATUS REDAÇÃO']).size().reset_index(name='Contagem Status')

                # Criando o mapa de calor de Status vs. Município com Altair
                heatmap_chart_status = alt.Chart(df_mapa_status).mark_rect().encode(
                    # Eixo X: Município (Nome da Prova)
                    x=alt.X('NOME MUN. PROVA', sort='y', title='Município de Prova'),
                    # Eixo Y: Status da Redação (Aprovado, Anulada, etc.)
                    y=alt.Y('STATUS REDAÇÃO', title='Status da Redação'),
                    # Cor: Contagem de Status (intensidade do calor)
                    color=alt.Color('Contagem Status', 
                                    # Usando uma escala de cores (heatmap) adequada para contagens
                                    scale=alt.Scale(range='viridis'), 
                                    title='Contagem'),
                    # Tooltip para exibir detalhes ao passar o mouse
                    tooltip=['NOME MUN. PROVA', 'STATUS REDAÇÃO', 'Contagem Status']
                ).properties(
                    # Título do gráfico e largura total
                    title="Contagem de Cada Status de Redação por Município",
                ).interactive() # Permite zoom e pan

                # Exibe o gráfico no Streamlit
                st.altair_chart(heatmap_chart_status, use_container_width=True)
    else:
                st.warning("Não é possível gerar o mapa de calor. As colunas 'NOME MUN. PROVA' e/ou 'STATUS REDAÇÃO' não foram encontradas.")
            
            
            # ----------------------------------------------------------------------
    # 3. Geração do Gráfico de Pizza (Proporção de Status)
    if status_exists:
                st.markdown("---")
                st.subheader("🥧 Proporção Total dos Status da Redação")

                # Reutiliza status_counts calculado anteriormente
                df_pizza = status_counts.reset_index(name='Contagem').rename(columns={'index': 'STATUS REDAÇÃO'})

                # Calcula a porcentagem para o tooltip
                total_count = df_pizza['Contagem'].sum()
                df_pizza['Porcentagem'] = (df_pizza['Contagem'] / total_count) * 100

                base = alt.Chart(df_pizza).encode(
                    theta=alt.Theta("Contagem", stack=True)
                )

                pie_chart = base.mark_arc(outerRadius=120).encode(
                    color=alt.Color("STATUS REDAÇÃO", title="Status"),
                    # Ordena as fatias por contagem (maior para menor)
                    order=alt.Order("Contagem", sort="descending"),
                    tooltip=["STATUS REDAÇÃO", "Contagem", alt.Tooltip("Porcentagem", format=".1f", title="Percentual")]
                ).properties(
                    title="Distribuição Percentual de Status"
                )

                # Adiciona texto no centro do gráfico (para um donut chart, mas funciona para pie)
                text = base.mark_text(radius=140).encode(
                    text=alt.Text("Porcentagem", format=".1f"),
                    order=alt.Order("Contagem", sort="descending"),
                    color=alt.value("black") # Define a cor do texto para melhor contraste
                )

                # Combina o gráfico de pizza e o texto
                final_chart = pie_chart.interactive()
                
                # Exibe o gráfico no Streamlit
                st.altair_chart(final_chart, use_container_width=True)

            # ----------------------------------------------------------------------
    # 4. Geração do Gráfico de Barras (Distribuição do Status da Redação)
    if 'STATUS REDAÇÃO' in df_filtrado.columns and not df_filtrado['STATUS REDAÇÃO'].empty:
                st.markdown("---")
                st.subheader("📊 Gráfico de Barras: Frequência Global do Status da Redação")

                # Cria o gráfico de barras
                bar_chart = alt.Chart(df_filtrado).mark_bar().encode(
                    # Eixo X: STATUS REDAÇÃO (Variável Categórica)
                    x=alt.X('STATUS REDAÇÃO', title='Status da Redação', sort='-y'),
                    # Eixo Y: Contagem de registros (frequência)
                    y=alt.Y('count()', title='Frequência (Contagem de Candidatos)'),
                    # Tooltip para interação
                    tooltip=[
                        alt.Tooltip('STATUS REDAÇÃO', title='Status'),
                        'count()'
                    ]
                ).properties(
                    title='Frequência dos Status da Redação no ENEM'
                ).interactive()

                st.altair_chart(bar_chart, use_container_width=True)
    else:
                st.info("Não é possível gerar o Gráfico de Barras. A coluna 'STATUS REDAÇÃO' não foi encontrada ou não possui dados válidos na seleção atual.")

            # ----------------------------------------------------------------------
        # 5. Geração do Gráfico de Barras Agrupadas (Comparação Status x Município)
    if not df_mapa_status.empty:
                st.markdown("---")
                st.subheader("📊 Comparação: Frequência de Status por Município")
                st.caption("Cada cor representa um município, e as barras mostram a contagem de cada Status da Redação.")

        # Cria o Gráfico de Barras Agrupadas
                grouped_bar_chart = alt.Chart(df_mapa_status).mark_bar().encode(
                    # Eixo X: Define a posição principal pelo Status
                    x=alt.X('STATUS REDAÇÃO', title='Status da Redação'),
                    # Eixo Y: Define a altura pela Contagem
                    y=alt.Y('Contagem Status', title='Contagem de Candidatos'),
                    # Cor: Define a cor pelo Município (o que queremos comparar)
                    color=alt.Color('NOME MUN. PROVA', title='Município'),
                    # xOffset: Desloca as barras dentro da mesma categoria STATUS REDAÇÃO, agrupando-as
                    xOffset='NOME MUN. PROVA',
                    tooltip=['STATUS REDAÇÃO', 'NOME MUN. PROVA', 'Contagem Status']
                ).properties(
                    title="Frequência de Status de Redação por Município"
                ).interactive()

                st.altair_chart(grouped_bar_chart, use_container_width=True)
    elif status_exists and 'NOME MUN. PROVA' in df_filtrado.columns:
                 st.info("Os dados para o Gráfico de Barras Agrupadas (Status x Município) não estão prontos. Verifique se os filtros estão aplicados corretamente.")
            # ----------------------------------------------------------------------
    st.markdown("---")
            