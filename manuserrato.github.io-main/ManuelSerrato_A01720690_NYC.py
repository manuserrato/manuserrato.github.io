import streamlit as st
import pandas as pd
import numpy as np

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')



@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

st.title('Paseos en bicicleta en New York City')

data_load_state = st.text('Cargando información del archivo de datos...')
data = load_data(1000)
data_load_state.text("Se logró cargar todo con éxito! (using st.cache)")

if st.sidebar.checkbox('Mostrar información en bruto'):
    st.subheader('Información cargada:')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Número de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


# Some number in the range 0-23
hour_to_filter = st.slider('HORA 0 - 23', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de todas las corridas a las %s:00 horas en New York City' % hour_to_filter)
st.map(filtered_data)
