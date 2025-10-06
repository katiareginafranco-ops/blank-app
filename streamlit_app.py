import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import altair as alt
from itertools import product

# Configuração da página com layout wide
st.set_page_config(page_title="Análise das Causas de Nota Zero na Redação do ENEM 2024", layout="wide")

# Carrega o CSV fixo
@st.cache_data
def carregar_csv_fixo():
    df = pd.read_csv("ENEM_ES_2024_REDAÇÃO.csv", encoding="utf-8")
    df.columns = df.columns.str.strip()
    return df

df = carregar_csv_fixo()

# Definições para domínios e filtros
status_todos = [1, 2, 3, 4, 6, 7, 8, 9]
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
mun_todos = sorted(df['NOME MUN. PROVA'].dropna().unique())
tipos_escola = sorted(df['DEP. ADMIN.'].dropna().unique())

# Layout: três colunas
sidebar1, main, sidebar2 = st.columns([1, 3, 1])

with sidebar1:
    st.sidebar.title("📑 Índice do App")
    st.sidebar.markdown("""
    - Visão Geral
    - Tabela Completa
    - Filtros Interativos
    - Gráficos
        """)

with sidebar2:
    st.sidebar.title("❓ Situações de Nota Zero")
    st.sidebar.markdown("""
    **1. 🚨 Fuga total ao tema:** texto fora do assunto proposto.  
    **2. 📄 Cópia dos textos motivadores:** redação que só reproduz textos de apoio.  
    **3. ✍️ Desenhos/Impropérios:** anotações, ofensas ou códigos indevidos.  
    **4. ⚖️ Desrespeito aos Direitos Humanos:** proposição que viola direitos humanos.  
    **5. 📚 Tipo textual errado:** não seguiu o modelo dissertativo-argumentativo.  
    **6. 📏 Menos de 8 linhas:** não atingiu o mínimo exigido.  
    **7. 🔗 Parte desconectada:** trechos sem relação com o tema.  
    **8. 📝 Folha em branco:** sem qualquer texto escrito.
    """)

with main:
    # Texto maior e estilizado
    st.markdown("<h1 style='font-size: 44px; font-weight: bold;'>Análise das Causas de Nota Zero na Redação do ENEM 2024</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 24px; font-style: italic; margin-bottom: 20px;'>Por: Kátia Regina Franco</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Explore os principais motivos que levam à nota zero nas redações, filtrando por município, status e tipo de escola.</p>", unsafe_allow_html=True)
    st.markdown("""
    <table style='font-size:18px; border-collapse: collapse; width: auto;'>
    <thead><tr><th style='border-bottom: 2px solid #ddd; padding: 8px;'>Código</th><th style='border-bottom: 2px solid #ddd; padding: 8px;'>Descrição</th></tr></thead>
    <tbody>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>1</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Sem problemas</td></tr>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>2</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Anulada</td></tr>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>3</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Cópia do texto motivador</td></tr>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>4</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Em branco</td></tr>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>6</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Fuga ao tema</td></tr>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>7</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Tipo textual errado</td></tr>
    <tr><td style='padding: 8px; border-bottom: 1px solid #ddd;'>8</td><td style='padding: 8px; border-bottom: 1px solid #ddd;'>Texto insuficiente</td></tr>
    <tr><td style='padding: 8px;'>9</td><td style='padding: 8px;'>Parte desconectada</td></tr>
    </tbody>
    </table>
    """, unsafe_allow_html=True)

    # Filtros - usados também na sidebar para manter alinhamento
    status_filtro = st.sidebar.multiselect(
        "Filtrar Status", status_todos, default=status_todos, format_func=lambda x: desc_status[x]
    )
    municipio_filtro = st.sidebar.multiselect(
        "Município", mun_todos, default=mun_todos
    )
    escola_filtro = st.sidebar.multiselect(
        "Tipo de Escola", tipos_escola, default=tipos_escola
    )

    df_filtrado = df[
        (df['NOME MUN. PROVA'].isin(municipio_filtro)) &
        (df['STATUS REDAÇÃO'].isin(status_filtro)) &
        (df['DEP. ADMIN.'].isin(escola_filtro))
    ]
# 🧾 Tabela completa 
    st.markdown("## 📄 Exibição da Tabela Completa Filtrada")
    st.dataframe(df_filtrado)
       
    st.dataframe(df_filtrado.style.set_table_styles([
        {'selector': 'th', 'props': [('font-size', '14pt'), ('padding', '4px 8px')]},
        {'selector': 'td', 'props': [('font-size', '12pt'), ('padding', '4px 8px')]},
        {'selector': '', 'props': [('max-width', '150px'), ('white-space', 'nowrap'), ('overflow', 'hidden'), ('text-overflow', 'ellipsis')]}
    ]), use_container_width=True)

    # Estatísticas resumidas
    status_counts = df_filtrado['STATUS REDAÇÃO'].value_counts()
    most_frequent_status = desc_status.get(status_counts.idxmax(), 'N/A') if not status_counts.empty else 'N/A'
    most_frequent_count = status_counts.max() if not status_counts.empty else 0
    least_frequent_status = desc_status.get(status_counts.idxmin(), 'N/A') if not status_counts.empty else 'N/A'
    least_frequent_count = status_counts.min() if not status_counts.empty else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Candidatos Filtrados", len(df_filtrado))
    col2.metric("Status Mais Frequente", most_frequent_status, delta=f"{most_frequent_count} registros")
    col3.metric("Status Menos Frequente", least_frequent_status, delta=f"{least_frequent_count} registros")

    # Preparação dos dados para gráficos
    todas_combs = pd.DataFrame(list(product(municipio_filtro, status_filtro)), columns=['NOME MUN. PROVA', 'STATUS REDAÇÃO'])
    df_mapa = df_filtrado.groupby(['NOME MUN. PROVA', 'STATUS REDAÇÃO']).size().reset_index(name='Contagem')
    df_mapa = todas_combs.merge(df_mapa, on=['NOME MUN. PROVA', 'STATUS REDAÇÃO'], how='left').fillna(0)
    df_mapa['Contagem'] = df_mapa['Contagem'].astype(int)
    df_mapa['DESC_STATUS'] = df_mapa['STATUS REDAÇÃO'].map(desc_status)

    municipios_ordenados = municipio_filtro if municipio_filtro else mun_todos
    status_ordenados = [desc_status[s] for s in status_filtro] if status_filtro else list(desc_status.values())

       # 📊 Gráfico de barras Matplotlib — Incidência do Status por Município (Stacked bar)
st.markdown("## 📍 Incidência do Status da Redação por Município")
incidencia = df_filtrado.groupby(['NOME MUN. PROVA', 'STATUS REDAÇÃO']).size().unstack(fill_value=0)

fig1, ax1 = plt.subplots(figsize=(12, 6))
incidencia.plot(kind='bar', stacked=True, ax=ax1)
ax1.set_title("Incidência do Status da Redação por Município")
ax1.set_xlabel("Município")
ax1.set_ylabel("Quantidade")
ax1.legend(title="Status", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.setp(ax1.get_xticklabels(), rotation=90)  # Rotaciona os rótulos no eixo X
plt.tight_layout()

st.pyplot(fig1)
   
    # 📊 Gráfico: Incidência do Status da Redação por Dependência Administrativa
st.markdown("## 📍 Incidência do Status da Redação por Dependência Administrativa")
import altair as alt

incidencia = df.groupby(['DEP. ADMIN.', 'STATUS REDAÇÃO']).size().reset_index(name='Contagem')

chart = alt.Chart(incidencia).mark_bar().encode(
    x=alt.X('DEP. ADMIN.:N', title='Dependência Administrativa'),
    y=alt.Y('Contagem:Q', title='Número de Redações'),
    color=alt.Color('STATUS REDAÇÃO:N', title='Status da Redação'),
    tooltip=['DEP. ADMIN.', 'STATUS REDAÇÃO', 'Contagem']
).properties(
    title='Incidência de Status da Redação por Dependência Administrativa'
).interactive()

st.altair_chart(chart, use_container_width=True)

# Exibe no Streamlit
st.pyplot(fig1)

st.markdown("---")
st.markdown("<p style='font-size:14px;'>Fonte de Dados: Microdados do ENEM, INEP.<br>Projeto de pós-graduação em Mineração de Dados Educacionais — UFES.</p>", unsafe_allow_html=True)