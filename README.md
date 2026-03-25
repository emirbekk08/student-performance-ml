  STUDENT PERFOMANCE PREDICTION

This is a simple machine learning web application built with Streamlit.

The app predicts a student's performance based on:
- study hours
- previous scores
- sleep hours
- extracurricular activities


  Project Files

- `app_01.py` — main web application (Streamlit interface)
- `train.py` — script to train the machine learning model
- `test.py` — script to test the model and display graphs
- `Student_Performance.csv` — dataset
- `requirements.txt` — required libraries

 How to run

 1. Clone the project

- git clone https://github.com/emirbekk08/student-performance-ml
- cd student-performance-ml
- pip install -r requirements.txt
- streamlit run app_01.py

.Train the model
python train.py

.Run test / show graph
python test.py
