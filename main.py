import streamlit as st
import requests
import urllib.parse

st.title('Gerador de latitude e longitude')

endereco = st.text_input(
        "Insira abaixo o endereço",
        "",
        key="logradouro",
    )

if st.button('Gerar Dados'):

        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(endereco) +'?format=json'

        response = requests.get(url).json()

        st.write("Latitude: ", response[0]["lat"])
        st.write("Longitude: ", response[0]["lon"])
