import pandas as pd 
import streamlit as st 
import pickle 

modelo_cargado = pickle.load(open('modelo_rf.pkl', 'rb'))


add_selectbox = st.sidebar.selectbox(' ', ('Pagina principal', 'Modelo Batch', 'Modelo csv'))


if add_selectbox == 'Pagina principal':
    st.image('cliente.png')
    st.title('Modelo de predicción de valor de cliente')
    st.text('Este modelo determina el valor de un cliente a partir de algunas caracteristicas observada')


if add_selectbox == 'Modelo Batch':
    st.title('Aqui puede realizar la predicción de cada uno de los clientes')
    Age = st.number_input('Ingrese aqui la edad', 
                          min_value=18,
                          max_value=99, 
                          value=45)
    compras = st.number_input('Ingrese el numero de compras promedio en el mes',
                              min_value=0,
                              max_value=150, 
                              value=10)
    gasto = st.number_input('Ingrese el gasto promedio del cliente en el mes',
                              min_value=0,
                              max_value=2000, 
                              value=20)
    Recency = st.number_input('Número de días desde que el cliente no realiza otra transacción',
                              min_value=0,
                              max_value=365, 
                              value=90)
    Income = st.number_input('Salario anual del cliente',
                              min_value=15000,
                              max_value=200000, 
                              value=38000)
    
    input_dict = {'Age':Age, 'compras': compras, 'gasto':gasto, 
                  'Recency': Recency, 'Income': Income}
    
    input_df = pd.DataFrame([input_dict])
    
    
    if st.button('Predicción'):
        salida = modelo_cargado.predict(input_df)
        output1 = int(salida)
        if output1 == 0:
            st.success('Este cliente es de: Muy Alto Valor')
        elif output1 ==3:
            st.success('Este cliente es de: Alto Valor')
        elif output1 ==2:
            st.success('Este cliente es de: Mediano Valor')
        else:
            st.success('Este cliente es de: Bajo Valor')
    

if add_selectbox =='Modelo csv':
    archivo_cargado = st.file_uploader('Ingrese aquí el archivo a predecir', type=['csv'])
    if archivo_cargado is not None:
        data_a_predecir = pd.read_csv(archivo_cargado, sep=';')
        data_a_predecir['Predicción'] = modelo_cargado.predict(data_a_predecir)
        st.write(data_a_predecir)