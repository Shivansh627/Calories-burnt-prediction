# importing dependencies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

# data collection and processing
# loading data from csv to pandas dataframe

calories = pd.read_csv('data/calories.csv')
exercise = pd.read_csv('data/exercise.csv')

#  checking the dataframes

print(calories.head(5))
print(exercise.head(5))

# combining the 2 dataframes

calories_data= pd.concat([exercise,calories['Calories']] ,axis=1)

# checking the dataframe

print(calories_data.head(5))

# checking the no. of rows and columns

print(calories_data.shape)

# getting some info about the data

print(calories_data.info())

# data analysis

print(calories_data.describe())

# data visualization

sns.set_theme()

sns.countplot(calories_data['Gender'])
plt.show()
sns.distplot(calories_data['Age'])
plt.show()
sns.distplot(calories_data['Height'])
plt.show()
sns.distplot(calories_data['Weight'])
plt.show()
sns.distplot(calories_data['Duration'])
plt.show()
sns.distplot(calories_data['Heart_Rate'])
plt.show()
sns.distplot(calories_data['Body_Temp'])
plt.show()
sns.distplot(calories_data['Calories'])
plt.show()


# finding correlation between data

numeric_data = calories_data.select_dtypes(include=['float64', 'int64'])
correlation = numeric_data.corr()

# cunstrocting a heatmap to understand correlation

plt.figure(figsize=(10,10))

sns.heatmap(correlation , cbar=True ,square=True ,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')
plt.show()

# watch video from 45 min

calories_data.replace({"Gender":{'male':0,'female':1}}, inplace=True)
calories_data.head()

X = calories_data.drop(columns=['User_ID','Calories'], axis=1)
Y = calories_data['Calories']

print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
# loading the model
model = XGBRegressor()

# training the model with X_train
model.fit(X_train, Y_train)
test_data_prediction = model.predict(X_test)

print(test_data_prediction)
mae = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("Mean Absolute Error = ", mae)