import streamlit as st
import pandas as pd
from PIL import Image

import matplotlib.pyplot as plt
import seaborn as sb

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

# визуализация представленных в датасете данных, используя контролы стримлита
st.divider()
st.header("Некоторая визуализация представленного датасета")


# сайдбар
st.sidebar.header("Фильтры данных для визуализации")
age_range = st.sidebar.slider("Возраст:",
                            min_value=int(df['Age'].min()),
                            max_value=int(df['Age'].max()),
                            value=(int(df['Age'].min()), 60))

selected_gender = st.sidebar.multiselect("Пол:",
                                    options=df['Gender'].unique(),
                                     default=df['Gender'].unique()
                                     )

bmi_range = st.sidebar.slider("Индекс массы тела (ИМТ):",
                                min_value=float(df['BMI'].min()),
                                max_value=float(df['BMI'].max()),
                                value=(float(df['BMI'].min()), 30.0))

upd_df = df[    # датафрейм после фильтрации слайдерами сайдбара
    (df['Age'].between(age_range[0], age_range[1])) &
    (df['Gender'].isin(selected_gender)) &
    (df['BMI'].between(bmi_range[0], bmi_range[1]))
]

# вкладки для визуализации отфильтрованных данных
metric_tab, distribution_tab, correlation_tab = st.tabs(["📈 Основные метрики", "📊 Распределения", "📉Корреляции"])