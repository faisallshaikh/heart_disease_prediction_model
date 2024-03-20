## Heart Disease Prediction Project

This project aims to predict the likelihood of heart disease based on various clinical features.

### Data Source

The dataset used in this project was sourced from a MySQL database containing anonymized patient data. 

It includes information such as age, sex, blood pressure, cholesterol levels, and other relevant clinical indicators.


### Data Processing

After retrieving the data from MySQL, the following processing steps were performed:

1. Data cleaning: Removed any missing or inconsistent values from the dataset.
2. Feature engineering: Derived new features from the existing ones, such as body mass index (BMI) from height and weight.
3. Exploratory data analysis (EDA): Investigated relationships between variables and identified potential patterns.
4. Feature scaling: Ensured uniform scaling of features to avoid dominance by certain variables.
5. Model training: Trained various machine learning models using the processed data to predict heart disease.

### Model Evaluation

The trained models were evaluated using cross-validation techniques to assess their performance in predicting heart disease. 
Metrics such as accuracy, precision, recall, and F1-score were calculated to measure the models' effectiveness.

### Usage

To run the project locally, follow these steps:
1. Clone the repository.
2. Install the necessary dependencies listed in the `requirements.txt` file.
3. Execute the main script (`main.py` or equivalent) to train the models and make predictions.

### Future Work

Future iterations of this project may involve:
- Incorporating additional data sources for improved prediction accuracy.
- Implementing advanced machine learning techniques, such as deep learning algorithms.
- Deploying the model as a web application or API for real-time predictions.


