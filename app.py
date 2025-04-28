import streamlit as st
import pandas as pd
from PIL import Image

# def show_dataset(): pass # определена в конце
st.set_page_config(page_title="ImDoc's Streamlit App", page_icon="❤️‍🩹",         
                    layout="wide",
                    initial_sidebar_state="auto",)

start_img = Image.open('src/health.png')
df = pd.read_csv('dataset/health_activity_data.csv')


st.title("Задание 1. Загрузка и отображение данных")

st.header("Health & Lifestyle Dataset")
st.image(start_img, width=600);

st.markdown("Датасет с `Kaggle`, содержащий информацию о *состоянии здоровья* и *стиле жизни* людей.")
df

st.markdown("""
В датасете содержится следующая информация:
- возраст `age`, пол `gender`, рост `Height_cm`, вес `Weight_kg`, имт `BMI`
- ежедневное количество шагов `Daily_Steps`
- потреблённые калории `Calories_Intake`
- количество часов сна `Hours_of_Sleep`
- сердечный ритм `Heart_Rate`
- кровяное давление `Blood_Pressure`
- время, уходящее на физические упражнения (часы в неделю) `Exercise_Hours_per_Week`
- является ли человек курильщиком `Smoker`
- употребление алкоголя (дней в неделю) `Alcohol_Consumption_per_Week`
- страдает ли человек диабетом `Diabetic`
- страдает ли от сердечных заболеваний `Heart_Disease`
""")


st.subheader("Некоторая визуализация представленного датасета")