import streamlit as st

# ---- Configuração da Página ----
st.set_page_config(
    page_title="Análise das Causas de Nota Zero na Redação do ENEM 2024",
    layout="centered"
)
coluna1, coluna2 = st.columns ((2, 1))
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
    st.subheader("O que leva uma redação a ser zerada?")
    st.markdown("""
        De acordo com a "Cartilha da Redação" do ENEM 2024, existem diversos motivos que
        podem anular um texto. São eles:
    """)
# ---- Seção de Análise Qualitativa (Cards) ----
    # Card 1: Fuga ao tema
    st.error("1. Fuga total ao tema", icon="🚨")
    st.markdown("""
        A redação deve abordar o tema proposto pelo ENEM. Se o texto foge completamente do
        assunto, o participante recebe nota zero.
    """)
    # Card 2: Cópia 
    st.warning("2. Cópia dos textos motivadores", icon="📄")
    st.markdown("""
        Copiar trechos dos textos de apoio (os chamados "textos motivadores")
        também anula a redação. O texto deve ser autoral, usando os textos motivadores
        apenas como referência.
    """)
    # Card 3: Anulada
    st.info("3. Anulada - Desenhos ou impropérios", icon="✍️")
    st.markdown("""
        Qualquer tipo de desenho, anotação indevida ou ofensa no espaço da redação, nome, assinatura, pode
        levar à anulação, já que pode ser um tipo de código para identificar o participante.
    """)
    # Card 4: Direitos Humanos
    st.success("4. Desrespeito aos Direitos Humanos", icon="⚖️")
    st.markdown("""
        A proposta de intervenção, que é um dos critérios de avaliação, não pode
        violentar os direitos humanos.
    """)
    # Card 5: Tipo textual
    st.error("5. Não atendimento ao tipo textual", icon="📚")
    st.markdown("""
        O texto precisa ser um "dissertativo-argumentativo". Qualquer outra forma,
        como poema, narração, ou receita, resulta em nota zero.
    """)
    # Card 6: Texto insuficiente
    st.warning("6. Texto com até 7 linhas", icon="📏")
    st.markdown("""
        A redação deve ter, no mínimo, 8 linhas escritas.
    """)
    # Card 7: Parte desconectada
    st.info("7. Texto com Parte desconectada ", icon="🔗")
    st.markdown("""
        A redação contém trechos sem relação com o tema proposto ou com o projeto de texto do candidato, atentando contra a seriedade da prova, tais como hino de time de futebol ou receita culinária.
    """)
    st.success("8. Folha de redação em branco", icon="📄")
    st.markdown("""
        A folha de redação não contém texto algum escrito.
    """)

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
st.caption("Próximos passos: Análise de dados quantitativos e visualização.")