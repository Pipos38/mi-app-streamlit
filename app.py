import streamlit as st
import random

st.title("Lanzador de Monedas")

num_lanzamientos = st.number_input("¿Cuántas veces quieres lanzar la moneda?", min_value=1, value=10)
if st.button("Lanzar"):
    resultados = ["Cara" if random.random() > 0.5 else "Cruz" for _ in range(int(num_lanzamientos))]
    st.write(resultados)
