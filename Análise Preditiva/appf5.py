# Importando as Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

from streamlit_option_menu import option_menu

# Configurações gerais da pagina do streamlit
st.set_page_config(layout="centered", page_title="Análise do Preço do Petróleo")

# Carregando dados
dados = pd.read_csv('C:/Users/Lucas/Documents/Projetos/alunos_merged.csv', sep=',')
# Como boa prática, para não interferir na base de dados original, foi criado um novo DataFrame chamado db, apenas copiando a base original, para que possamos trabalhar
db = dados
# Pelo .info() duas linhas acima, vimos que váris colunas que deveriam ser números inteiros ou números float estão classificadas como objetos, portanto precisamos corrigir seus formatos
# Conferir as colunas a serem convertidas
cols_to_convert = ["Fase",'IAA', 'IAN', 'IDA', 'IEG', 'INDE', 'IPP', 'IPS', 'IPV']
# Converter as colunas de texto para valores numéricos
db[cols_to_convert] = db[cols_to_convert].apply(pd.to_numeric, errors='coerce')
# Como nossa variável de saída é a Pedra, não podemos ter valores nulos/vazios nela, então irei dar um dropna e criar um outro DataFrame em que conste somente as células com valor
db_full = db.dropna(subset=["Pedra"])
db_full = db_full[(db_full["Pedra"] != "#NULO!") & (db_full["Pedra"] != "D9891/2A") & (db_full["DataNascimento"] != "M")]
# Com a base limpa, irei agora preencher as lacunas de valores que ainda permaneceram nas colunas de notas e preencherei com um valor médio nesses respectivos campos
cols_to_fill = ['IAA', 'IAN', 'IDA', 'IEG', 'INDE', 'IPP', 'IPS', 'IPV']
# As preencho com a média
db_full[cols_to_fill] = db_full[cols_to_fill].fillna(db_full[cols_to_fill].mean())
#Em seguida já aproveito para substituir os nomes de cada pedra para números, já preparando os dados para a aplicação do xgboost posteriormente, que irá trabalhar apenas com dados numéricos
label_encoder = LabelEncoder()
db_full["Pedra"] = label_encoder.fit_transform(db_full["Pedra"])
db_full["Idade"] = db_full["Ano"] - db_full["DataNascimento"].str[:4].astype(int)

#Variaveis que serao utilizados para os modelos de predicao
x_1 = db_full[['INDE','Fase','Idade']]
y_1 = db_full['Pedra']

X_train, X_test, y_train, y_test = train_test_split(x_1, y_1, test_size=0.2, random_state=42)

# Menu lateral
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Participantes", "Introdução", "Desenvolvimento"],
        icons=["people-fill", "book-fill", "book-fill", "bar-chart-fill", "list-columns-reverse"],
        menu_icon="grid-fill",
        default_index=0,
    )

# Seção: Participantes
if selected == "Participantes":
    st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="margin-bottom: 1rem;">FIAP - PÓS TECH - DATA ANALYTICS</h1>
        <h2 style="margin-bottom: 1rem;">FASE 5 - DATATHON</h2>
        <h3 style="margin-bottom: 1rem;">TURMA 5DTAT - GRUPO 44</h3>
        <h4 style="margin-bottom: 2rem;">INTEGRANTES</h4>
        <p style="font-size: 20px; line-height: 1.5;">
            Gabriel Silva Ferreira<br>
            Gustavo Duran Domingues<br>
            Jhonny Amorim Silva<br>
            Lucas Alexander dos Santos<br>
            Sandro Semmer
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )

# Seção: Introdução
if selected == "Introdução": 
    st.markdown(
            """
            <div style="text-align: left;">
                <p style="font-size: 20px; line-height: 1.5;">
                O acesso à educação de qualidade é um direito fundamental e um pilar para a transformação social, especialmente para jovens em situação de vulnerabilidade. 
                É nisso que a  associação Passos Mágicos  emerge como exemplo de um projeto social e educacional que busca instrumentalizar o uso da educação como ferramenta 
                para a mudança das condições de vida das crianças e jovens em vulnerabilidade social que residem no Embu Guaçu - Município de São Paulo, através da educação 
                de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo.<br>
                O presente trabalho tem como objetivo analisar o impacto da atuação da Passos Mágicos na trajetória educacional de seus estudantes. 
                Por meio da coleta e análise de dados sobre o desempenho acadêmico, frequência e participação nas atividades oferecidas pela organização, busca-se identificar 
                os indicadores de performance que melhor refletem o progresso dos jovens atendidos. Adicionalmente, a  análise preditiva visa levantar padrões e tendências 
                que possam subsidiar o aprimoramento das práticas pedagógicas da Passos Mágicos, contribuindo para o fortalecimento de sua missão de transformar vidas por 
                meio da educação.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Seção: Desenvolvimento
if selected == "Desenvolvimento":
    st.title("Análise do Modelos de Machine Learning")     

    opcao = st.selectbox(
        "Escolha uma opção:",
        ["XGBoost", "Decision Tree"]
    )

    # Decision Tree
    if opcao == "Decision Tree":
        st.markdown(
            """
            <div style="text-align: center;">
                <p style="font-size: 20px; line-height: 1.5;">
                Modelo de Árvore de Decisão<br>
                Uma árvore de decisão é um modelo de machine learning baseado em uma estrutura hierárquica de decisões. 
                Ele divide os dados em subconjuntos menores com base em condições de variáveis preditoras, gerando um conjunto de regras simples que ajudam na classificação ou previsão.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        modelo = DecisionTreeClassifier(max_depth=5, random_state=7)
        modelo.fit(X_train, y_train)
        previsoes = modelo.predict(X_test)
        acuracia = accuracy_score(y_test, previsoes)
        st.write(f"Acurácia: {acuracia * 100:.2f}%")

        INDE = st.number_input('Insira o INDE', key='num1')
        FASE = st.number_input('Insira a Fase', key='num2')
        ANO = st.number_input('Insira a Idade', key='num3')

        if INDE != 0 and FASE != 0 and ANO != 0:
            if st.button("Fazer Previsão"):
                input_data = np.array([[INDE, FASE, ANO]])
                resultado = modelo.predict(input_data)
                y_pred_categoria = label_encoder.inverse_transform(resultado.astype(int))
                st.write(f"A previsão para a variável 'Pedra' é: {y_pred_categoria[0]}")

                # Exibir a árvore de decisão
                fig, ax = plt.subplots(figsize=(12, 8))
                plot_tree(modelo, filled=True, ax=ax)
                st.pyplot(fig)
        else:
            st.write("Por favor, insira valores válidos para todos os campos.")

 # XGBoost
    if opcao == "XGBoost":
        st.write("")
        
        st.markdown(
            """
            <div style="text-align: center;">
                <p style="font-size: 20px; line-height: 1.5;">
                    Modelo XGBoost<br>
                    O XGBoost é um dos algoritmos de aprendizado de máquina mais populares, baseado em árvores de decisão, que utiliza o método de boosting.
                    No boosting, várias árvores de decisão simples (modelos fracos) são treinadas de forma sequencial, onde cada árvore tenta corrigir os erros cometidos pelas anteriores.
                    Isso torna o modelo altamente eficiente e robusto.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        modelo_xgb = XGBClassifier(random_state=42)
        modelo_xgb.fit(X_train, y_train)
        previsoes_xgb = modelo_xgb.predict(X_test)
        acuracia_xgb = accuracy_score(y_test, previsoes_xgb)
        st.write(f"Acurácia do XGBoost: {acuracia_xgb * 100:.2f}%")

        INDE = st.number_input('Insira o INDE', key='num1_xgb')
        FASE = st.number_input('Insira a Fase', key='num2_xgb')
        ANO = st.number_input('Insira a Idade', key='num3_xgb')

        if INDE != 0 and FASE != 0 and ANO != 0:
            if st.button("Fazer Previsão XGBoost"):
                input_data_xgb = np.array([[INDE, FASE, ANO]])
                resultado_xgb = modelo_xgb.predict(input_data_xgb)
                y_pred_categoria_xgb = label_encoder.inverse_transform(resultado_xgb.astype(int))
                st.write(f"A previsão para a variável 'Pedra' com XGBoost é: {y_pred_categoria_xgb[0]}")
        else:
            st.write("Por favor, insira valores válidos para todos os campos.")

