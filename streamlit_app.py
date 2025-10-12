import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Configuração da página com tema e layout wide
st.set_page_config(page_title="Análise das Causas de Nota Zero na Redação do ENEM 2024", layout="wide")

# Carregamento da base de dados fixa
@st.cache_data
def carregar_csv_fixo():
    df = pd.read_csv("ENEM_ES_2024_REDAÇÃO.csv", encoding="utf-8")
    df.columns = df.columns.str.strip()
    return df

df = carregar_csv_fixo()
df = df.dropna(subset=['STATUS REDAÇÃO'])

# Dicionários para status e tipo de escola
desc_status = {
    1: "Sem problemas",
    2: "Anulada",
    3: "Cópia do texto motivador",
    4: "Em branco",
    6: "Fuga ao tema",
    7: "Tipo textual errado",
    8: "Texto insuficiente",
    9: "Parte desconectada"
}

dep_admin_dict = {
    1: "Federal",
    2: "Estadual",
    3: "Municipal",
    4: "Privada"
}

# Listas para seleção de filtros
status_todos = list(desc_status.keys())
mun_todos = sorted(df['NOME MUN. PROVA'].dropna().unique())
dep_admin_todos = list(dep_admin_dict.keys())

# Layout com 2 colunas (sidebar_col para filtros, main_col para conteúdo)
sidebar_col, main_col = st.columns([1, 3])

with sidebar_col:
    st.title("📑 Índice do App")
    st.markdown("""
- Apresentação
- Tabela Completa
- Filtros Interativos
- Gráficos
""")
    st.markdown("### Selecione os filtros para os gráficos:")

    # Filtros interativos com multiselect
    with st.expander("Filtros de status", expanded=True):
        status_filtro = st.multiselect(
            "Status da Redação",
            status_todos,
            default=status_todos,
            format_func=lambda x: desc_status.get(x, str(x))
        )

    with st.expander("Filtros de município", expanded=True):
        municipio_filtro = st.multiselect(
            "Município",
            mun_todos,
            default=mun_todos
        )

    with st.expander("Filtros de escola", expanded=True):
        escola_filtro = st.multiselect(
            "Tipo de Escola",
            dep_admin_todos,
            default=dep_admin_todos,
            format_func=lambda x: dep_admin_dict.get(x, str(x))
        )

# Limpeza de eventuais valores nan no status
status_filtro_limpo = [s for s in status_filtro if not (isinstance(s, float) and math.isnan(s))]

# Filtragem dos dados baseados nos filtros
df_filtrado = df[
    (df['NOME MUN. PROVA'].isin(municipio_filtro)) &
    (df['STATUS REDAÇÃO'].isin(status_filtro_limpo)) &
    (df['DEP. ADMIN.'].isin(escola_filtro))
]

with main_col:
    # Títulos e textos formatados
    st.markdown("<h1 style='font-size: 44px; font-weight: bold;'>Análise das Causas de Nota Zero na Redação do ENEM 2024</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 28px; font-style: italic; margin-bottom: 20px;'>Por: Kátia Regina Franco</p>", unsafe_allow_html=True)

    st.markdown(
        "<p style='font-size: 34px;'>Bem-vindo ao protótipo de análise das redações do ENEM 2024. "
        "Aqui, você pode explorar e entender os principais motivos que levam as redações a receberem a nota zero, uma situação que pode ser evitada com informação e estudo. "
        "Neste aplicativo, vamos desmistificar os critérios de anulação para ajudar estudantes e educadores a se prepararem melhor. "
        "Embora o recorte se dê nos resultados do estado do Espírito Santo, estudantes de outros estados também podem utilizar as informações. "
        "Além da análise de todo o estado, você pode explorar os principais motivos que levaram à nota zero nas redações Enem 2024 selecionando os filtros de seu interesse: por município, status e tipo de escola.</p>", 
        unsafe_allow_html=True
    )

    st.subheader("📊 Redação ENEM 2024: Por que a Nota Zero?")
    st.markdown(
        "<p style='font-size: 26px;'>Conheça e entenda as situações das redações avaliadas no Enem 2024 no quadro abaixo.</p>", 
        unsafe_allow_html=True
    )

    # Tabela HTML informativa sobre status da redação
    html_table = """
    <table style='font-size:18px; border-collapse: collapse; width: auto;'>
    <thead>
      <tr>
        <th style='border-bottom: 2px solid #ddd; padding: 8px; text-align: center;'>Código</th>
        <th style='border-bottom: 2px solid #ddd; padding: 8px; text-align: center;'>Descrição</th>
        <th style='border-bottom: 2px solid #ddd; padding: 8px; text-align: center;'>Sentido</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>1</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Sem problemas</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'> ✔️Redação corrigida normalmente, pois todos os requisitos foram cumpridos.</td>
      </tr>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>2</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Anulada</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>&#x270D; Presença de desenhos, impropérios, ofensas ou códigos indevidos.</td>
      </tr>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>3</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Cópia do texto motivador</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>📄 Cópia dos textos motivadores, ou seja, redação que só reproduz os textos de apoio.</td>
      </tr>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>4</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Em branco</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>📝 Folha em branco, sem qualquer texto escrito.</td>
      </tr>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>6</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Fuga ao tema</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>🚨 Texto fora do assunto proposto.</td>
      </tr>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>7</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Tipo textual errado</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>📚 A estrutura da redação não seguiu o modelo dissertativo-argumentativo.</td>
      </tr>
      <tr>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>8</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>Texto insuficiente</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>📏 A redação possui menos de 8 linhas, não atingindo o mínimo exigido.</td>
      </tr>
      <tr>
        <td style='padding: 8px;'>9</td>
        <td style='padding: 8px;'>Parte desconectada</td>
        <td style='padding: 8px; border-bottom: 1px solid #ddd;'>🔗 Trechos sem relação com o tema ou com o projeto de texto, como música e receita.</td>
      </tr>
    </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

    # Estatísticas da base utilizando describe()
    st.subheader("Tabela Descritiva da Base de Dados")
    st.dataframe(df_filtrado.describe(include='all'))

    # Quantidade de linhas (participantes)
    total_participantes = len(df_filtrado)
    st.markdown(f"**Quantidade de Participantes:** {total_participantes}")

    # Incidência do status da redação em ordem decrescente
    incid_status = df_filtrado['STATUS REDAÇÃO'].value_counts().sort_values(ascending=False)
    st.markdown("**Incidência de Status da Redação (ordem decrescente):**")
    st.dataframe(pd.DataFrame(incid_status))

    st.markdown("---")

    # Gráfico 1: Incidência do Status de Redação por Município (Stacked Bar)
    st.subheader("Incidência do Status de Redação por Município")
    # Criar tabela cruzada para stacked bar
    pivot_mun_status = pd.crosstab(df_filtrado['NOME MUN. PROVA'], df_filtrado['STATUS REDAÇÃO'])
    pivot_mun_status = pivot_mun_status[status_todos]  # manter ordem dos status

    # Plot stacked bar chart
    fig1, ax1 = plt.subplots(figsize=(14,8))
    pivot_mun_status.plot(kind='bar', stacked=True, ax=ax1, colormap='tab20')
    ax1.set_ylabel('Quantidade de Redações')
    ax1.set_xlabel('Município')
    ax1.set_title('Incidência do Status de Redação por Município')
    ax1.legend([desc_status.get(i, str(i)) for i in pivot_mun_status.columns], title='Status Redação', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig1)

    # Gráfico 2: Incidência do Status da Redação por Dependência Administrativa
    st.subheader("Incidência do Status da Redação por Dependência Administrativa")
    pivot_dep_status = pd.crosstab(df_filtrado['DEP. ADMIN.'], df_filtrado['STATUS REDAÇÃO'])
    pivot_dep_status = pivot_dep_status[status_todos]  # manter ordem dos status

    fig2, ax2 = plt.subplots(figsize=(10,6))
    pivot_dep_status.plot(kind='bar', stacked=True, ax=ax2, colormap='tab20')
    ax2.set_ylabel('Quantidade de Redações')
    ax2.set_xlabel('Dependência Administrativa')
    ax2.set_title('Incidência do Status da Redação por Dependência Administrativa')
    ax2.set_xticklabels([dep_admin_dict.get(i, str(i)) for i in pivot_dep_status.index], rotation=0)
    ax2.legend([desc_status.get(i, str(i)) for i in pivot_dep_status.columns], title='Status Redação', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig2)

    # Fonte dos dados
    st.markdown("---")
    st.markdown("<p style='font-size:14px;'>Fonte de Dados: Microdados do ENEM, INEP.<br>Projeto de pós-graduação em Mineração de Dados Educacionais — UFES.</p>", unsafe_allow_html=True)
