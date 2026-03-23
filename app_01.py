import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. ПОДГОТОВКА (Данные и Модель)
st.set_page_config(layout="wide")
df = pd.read_csv("Student_Performance.csv")
df["Extracurricular Activities"] = df["Extracurricular Activities"].map({"Yes": 1, "No": 0})

X = df.drop(columns=["Performance Index"])
y = df["Performance Index"]
model = LinearRegression().fit(X.values, y)

# 2. ИНТЕРФЕЙС (Одна страница)
st.title("Linear Regression")
st.title("🎓 Student Performance Dashboard")

col1, col2 = st.columns([1, 1.5], gap="large")  # Левая колонка для ввода, правая для визуала

with col1:
    st.subheader("📝 Data entry")
    h = st.number_input("Hours Studied", 1, 10, 5)
    s = st.number_input("Previous Scores", 40, 100, 70)
    sl = st.number_input("Sleep Hours", 4, 10, 7)
    p = st.number_input("Sample Papers", 0, 10, 5)
    a = 1 if st.selectbox("Extra Activities", ["Yes", "No"]) == "Yes" else 0

    if st.button("Predict Result", type="primary", use_container_width=True):
        res = model.predict([[h, s, sl, p, a]])
        st.success(f"**Predicted Index: {res[0]:.2f}**")

with col2:
    # Блок с графиком
    st.subheader("📊 Model accuracy")
    fig, ax = plt.subplots(figsize=(5, 2.5))  # Очень компактный размер
    y_p = model.predict(X[:100].values)
    ax.scatter(y[:100], y_p, alpha=0.5, s=10, color="dodgerblue")
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r', lw=1)
    st.pyplot(fig)

    # Блок с таблицей под графиком
    st.subheader("📋 Date (Top 20)")
    st.dataframe(df.head(21), use_container_width=True, height=300)

