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
st.divider()

st.header("Health & Lifestyle Dataset")
st.image(start_img, width=700);

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
metric_tab, distribution_tab, correlation_tab = st.tabs(["📈 Показатели", "📊 Распределения", "📉Корреляции"])

# метрики (значения по полу в датасете и зависимость между ИМТ и возрастом)
with metric_tab:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Средние показатели по полу в датасете")

        stats_by_gender = upd_df.groupby('Gender')[['Height_cm','Weight_kg', 'Hours_of_Sleep', 'Exercise_Hours_per_Week', 'Heart_Rate']].mean()
        st.bar_chart(stats_by_gender)

        st.write("Столбчатая диаграмма значений роста, веса, часов сна, часов физических упражнений, сердечного ритма людей, выбранного пола.")

    with col2:
        st.subheader("Зависимость ИМТ от возраста:")

        figure, axes = plt.subplots()
        sb.scatterplot(data=upd_df, x='Age', y='BMI', hue='Gender', ax=axes)
        st.pyplot(figure)

        st.write("Точечный график зависимости между ИМТ и возрастом с обозначением пола цветом.")



with distribution_tab:
    st.subheader("Распределение анализируемых показателей")
    st.write("Построение гистограммы распределения вместе с кривой плотности для выбранного показателя с разделением по полу.")
    
    selected_column = st.selectbox(
        "Выберите показатель:",
        ['Daily_Steps', 'Hours_of_Sleep', 'Exercise_Hours_per_Week', 'Heart_Rate']
    )
    figure, axes = plt.subplots()
    sb.histplot(data=upd_df, x=selected_column, kde=True, hue='Gender', multiple='stack')
    st.pyplot(figure)



with correlation_tab:
    st.subheader("Матрица корреляций")
    st.write("Построение матрицы корреляции, тепловой карты (синий - отрицательные значения, красный - положительные) для всех числовых значений в отфильтрованном датасете")

    numeric_cols = upd_df.select_dtypes(include=['float64', 'int64']).columns
    corr_matrix = upd_df[numeric_cols].corr()
    
    figure, axes = plt.subplots(figsize=(10,8))
    sb.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=axes)
    st.pyplot(figure)