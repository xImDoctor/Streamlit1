import streamlit as st
import pandas as pd

# def show_dataset(): pass # определена в конце
st.set_page_config(page_title="ImDoc's Streamlit App", page_icon="📃")


st.title("Задание 1. Загрузка и отображение данных")
st.header("Health & Lifestyle Dataset")
st.markdown("Датасет с `Kaggle`, содержащий информацию о *состоянии здоровья* и *стиле жизни* человека")

df = pd.read_csv('dataset/health_activity_data.csv')
df

st.markdown("""
В дасете содержится следующая информация:
- физическая активность
- количество часов сна
- психическое (ментальное) здоровье
- медицинские данные (история заболеваний)
""")
