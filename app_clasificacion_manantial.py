import pandas as pd
import streamlit as st
import pickle

st.set_page_config(page_title="Clasificación de manantiales en Colombia, a partir de un modelo de regresión logística.",
                   layout="centered",
                   initial_sidebar_state="auto")

st.title("Clasificación de manantiales en Colombia, a partir de un modelo de regresión logística")
st.write("Para clasificar los manantiales se usan los datos suministrados por el servicio geologico colombiano, se usan 127 puntos, las varaibles descriptoras son: caudal, temperatura, olor, conductividad eléctrica, ph in situ, para entrenar y validar el modelo se usan manantiales previamente clasificados en clorurados y sulfatados, se usa un modelo de machine learning; regresión logística que permité clasificar los manantiales arrojando un accuracy de 0.61")
st.title("Modelo de regresión logística")
st.write("La regresión logística es un algoritmo de aprendizaje supervisado utilizado para la clasificación binaria. Predice la probabilidad de que una observación pertenezca a una de dos clases posibles. En lugar de predecir valores continuos como la regresión lineal, utiliza la función sigmoide para modelar la probabilidad de la clase objetivo.")
st.title("Desarrollo de la aplicación")
st.write('Para desarrollar la aplicación, se usa el archivo "datos_manantiales.csv", la cual contiene 5 variables a partir de los cuales se va a generar el modelo. Para el despliegue se usa la libreria streamlit de python que permite desarrollar aplicaciones web a partir de modelos de inteligencia artificial de forma ágil.')
st.title('Indicaciones para usar la app')
st.write("En la sección lateral de la izquierda se encuentra cuatro barras deslizantes que representan cada variable del modelo. Al modificar las barras, el modelo clasificará los manantiales en clorurado y sulfatado según corresponda.")
st.sidebar.header("Datos suministrados por el usuario")
def user_input_features():
    Caudal = st.sidebar.slider('Caudal',0,1,0)
    temperature = st.sidebar.slider('Temperatura',0,1,0)
    olor = st.sidebar.slider('Olor',0,1,0)
    conductividad = st.sidebar.slider('conductividad_electrica',0,1,0)
    ph = st.sidebar.slider('ph_insitu',0,1,0)
    data ={"CAUDAL":Caudal,
            "TEMPERATUR":temperature,
            "OLOR": olor,
            "CONDUCTIVIDAD_ELECTRICA":conductividad,
            "PH_IN_SITU":ph
           }
    features = pd.DataFrame(data,index=[0])
    return features
input_df = user_input_features()

st.write("Datos ingresados")
st.write(input_df)
load_clf =pickle.load(open('reg_log_manantiales.pkl','rb'))

prediction = load_clf.predict(input_df)


highlight_css = """
<div style="
    border: 2px solid #4CAF50; 
    padding: 10px; 
    border-radius: 10px; 
    background-color: #f9f9f9; 
    text-align: center; 
    font-size: 24px; 
    font-weight: bold; 
    color: #4CAF50;
">
    {0}
</div>
"""

# Mostrar el dato enmarcado y resaltado

st.write("con base en los parametros escogidos la anomalía magnética se estima en:")
st.markdown(highlight_css.format(prediction[0]), unsafe_allow_html=True)





