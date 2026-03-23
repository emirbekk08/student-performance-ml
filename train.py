import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# 1) Загрузка
df = pd.read_csv("Student_Performance.csv")
# Extracurricular Activities
df["Extracurricular Activities"] = df["Extracurricular Activities"].map({"Yes": 1, "No": 0})
TARGET = "Performance Index"
X = df.drop(columns=[TARGET])
y = df[TARGET]

# 4) Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 5) Модель
model = LinearRegression()
model.fit(X_train, y_train)
# 6) Предсказание
y_pred = model.predict(X_test)

# сохранение модели
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved!")


# 7) Метрики
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"MAE  = {mae:.3f}")
print(f"RMSE = {rmse:.3f}")
print(f"R2   = {r2:.3f}")
print("Y unique values:", sorted(y.unique())[:20])
print("COLUMNS:", df.columns.tolist())
print("TARGET col name exists:", "Performance Index" in df.columns)
print("\nTARGET stats:")
print(df["Performance Index"].describe())
print("First 10 target values:", df["Performance Index"].head(10).tolist())
print("Unique target sample:", sorted(df["Performance Index"].unique())[:20])

# 9) График: реальное vs предсказанное
plt.figure()
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(),y_test.max()], [y_pred.min(), y_pred.max()], color="red")
plt.xlabel("Real Performance Index")
plt.ylabel("Predicted Performance Index")
plt.title("Linear Regression: Real vs Predicted")
plt.show()
