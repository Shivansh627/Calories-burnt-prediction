Calories Prediction using XGBoost


This project aims to predict the number of calories burned based on exercise-related features, using the XGBoost regression model. The dataset contains information about individuals' exercises, such as their gender, age, height, weight, exercise duration, heart rate, and body temperature, alongside the calories burned during the exercise.

Project Structure
calories.csv: Contains data on calories burned by individuals.
exercise.csv: Contains data on exercise characteristics of individuals.
Steps Involved
Data Collection & Loading:

Data is loaded from CSV files into pandas DataFrames (calories.csv and exercise.csv).
Data Preprocessing:

The two datasets (exercise and calories) are merged.
The 'Gender' column is encoded (male = 0, female = 1).
Exploratory Data Analysis (EDA):

Descriptive statistics and visualizations (histograms, count plots) are generated to understand the distribution of features like Age, Height, Weight, Duration, Heart Rate, Body Temperature, and Calories.
Correlation Analysis:

Correlation between numeric features is visualized using a heatmap to identify relationships between variables.
Feature Selection:

The dataset is split into features (X) and target variable (Y), with Y being the 'Calories' column.
Model Training:

The dataset is split into training and testing sets (80% for training and 20% for testing).
An XGBRegressor model is used to predict the calories burned based on the exercise data.
Model Evaluation:

Mean Absolute Error (MAE) is calculated to evaluate the model's performance.
Dependencies
The following libraries are used in this project:

numpy
pandas
matplotlib
seaborn
scikit-learn
xgboost
You can install them using pip:

bash
Copy code
pip install numpy pandas matplotlib seaborn scikit-learn xgboost

Output
Mean Absolute Error (MAE) is calculated to assess the model's prediction accuracy.
Conclusion
This project demonstrates how to predict calories burned during exercise using a machine learning model (XGBoost). It involves data preprocessing, visualization, model training, and evaluation.
