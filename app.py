import streamlit as st
import pandas as pd
from PIL import Image

# def show_dataset(): pass # определена в конце
st.set_page_config(page_title="ImDoc's Streamlit App", page_icon="❤️‍🩹")

start_img = Image.open('src/health.png')
df = pd.read_csv('dataset/health_activity_data.csv')


st.title("Задание 1. Загрузка и отображение данных")

st.header("Health & Lifestyle Dataset")
st.image(start_img);

st.markdown("Датасет с `Kaggle`, содержащий информацию о *состоянии здоровья* и *стиле жизни* человека.")
df

st.markdown("""
В датасете содержится следующая информация:
- возраст, пол, рост, вес, имт (bmi)
- физическая активность (количество шагов, сожжённых калорий)
- количество часов сна
- психическое (ментальное) здоровье
- медицинские данные (история заболеваний)
""")
