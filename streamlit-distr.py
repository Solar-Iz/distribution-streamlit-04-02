import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, poisson

st.title("Визуализация кривых распределений")

# Выбор распределения
distribution = st.selectbox("Выберите распределение:", ("Нормальное", "Экспоненциальное", "Пуассона"))

# Параметры распределения
if distribution == "Нормальное":
    mean = st.number_input("Среднее (μ)", value=0.0)
    std_dev = st.number_input("Стандартное отклонение (σ)", value=1.0)
elif distribution == "Экспоненциальное":
    scale = st.number_input("Параметр масштаба (λ)", value=1.0)
elif distribution == "Пуассона":
    mu = st.number_input("Среднее (μ)", value=1.0)
    range_max = st.number_input("Максимальное значение диапазона", value=10)  # Добавляем параметр range_max

# Генерация данных и построение графика
if st.button("Построить график"):
    if distribution == "Нормальное":
        x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
        y = norm.pdf(x, loc=mean, scale=std_dev)
    elif distribution == "Экспоненциальное":
        x = np.linspace(0, scale * 5, 1000)  # Увеличиваем диапазон для экспоненциального распределения
        y = expon.pdf(x, scale=scale)
    elif distribution == "Пуассона":
        x = np.arange(0, range_max)  # Используем range_max для диапазона Пуассона
        y = poisson.pmf(x, mu)

    plt.plot(x, y)
    plt.xlabel("Значение случайной величины")
    plt.ylabel("Плотность вероятности")
    st.pyplot(plt)

# Очистка графика
if st.button("Очистить график"):
    st.empty()