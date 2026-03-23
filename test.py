import pickle
import numpy as np

def get_float(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Пожалуйста, напишите числом!")

def get_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Пожалуйста, напишите числом!")

with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Enter student data")

hours = get_float("Hours Studied: ")
previous = get_float("Previous Scores: ")
sleep = get_float("Sleep Hours: ")
activities = get_int("Extracurricular Activities (1 yes / 0 no): ")
papers = get_float("Sample Question Papers Practiced: ")

data = np.array([[hours, previous, activities, sleep, papers]])

prediction = model.predict(data)

print("Predicted Performance Index:", prediction[0])