import streamlit as st
import pandas as pd
import numpy as np



st.title('Netflix App')

DATE_COLUMN = 'released'
DATA_URL = ('movies.csv')

import codecs

@st.cache_data
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_filme(filme):
    filtered_data_filme = data[data['name'].str.upper().str.contains(filme)]
    return filtered_data_filme

def filter_data_by_director(director):
    filtered_data_director = data[data['director'] == director]
    return filtered_data_director




data_load_state = st.text('Cargando los datos...')
data = load_data(500)
data_load_state.text("Se logró cargar todo con éxito! (using st.cache)")

if st.sidebar.checkbox('Mostrar todas las películas'):
    st.subheader('Todas las películas')
    st.write(data)


titulofilme = st.sidebar.text_input('Título de la película :')
btnBuscar = st.sidebar.button('Buscar películas')

if (btnBuscar):
   data_filme = filter_data_by_filme(titulofilme.upper())
   count_row = data_filme.shape[0]  
   st.write(f"Total filmes mostrados : {count_row}")
   st.write(data_filme)



selected_director = st.sidebar.selectbox("Seleccionar el director", data['director'].unique())
btnFilterbyDirector = st.sidebar.button('Filtrar por director ')

if (btnFilterbyDirector):
   filterbydir = filter_data_by_director(selected_director)
   count_row = filterbydir.shape[0]  
   st.write(f"Total filmes : {count_row}")

   st.dataframe(filterbydir)
