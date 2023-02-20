import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

exercise_data = pd.read_csv('exercise_data.csv')

# Loaing the user data
age = input('Please enter your age: ')
height = input('Please enter your height (in centimeters): ')
weight = input('Please enter your weight (in kilograms): ')

# Creating a user profile based on the user's personal information
user_profile = {
    'age': int(age),
    'height': int(height),
    'weight': int(weight)
}

# Printing the user profile
print('Your user profile:')
print(user_profile)

# Asking the user for their workout preferences
muscle_group = input('Which muscle group would you like to target? ')
num_sets = input('How many sets would you like to do? ')
num_reps = input('How many reps would you like to do per set? ')

# Converting the input values to numeric data types
weight = float(weight)
num_sets = int(num_sets)
num_reps = int(num_reps)

# Creating a workout plan based on the user's preferences and body type
workout_plan = exercise_data[(exercise_data['muscle_group'] == muscle_group) & (exercise_data['weight'] <= user_profile['weight'])]

# Shuffling the workout plan
workout_plan = workout_plan.sample(frac=1)

# Spliting the workout plan into training and testing sets
train, test = train_test_split(workout_plan, test_size=0.2)

# Creating a linear regression model
model = LinearRegression()

# Training the model on the training data
model.fit(train[['weight', 'num_sets', 'num_reps']].astype(float), train['calories_burned'])

# Testing the model on the testing data
score = model.score(test[['weight', 'num_sets', 'num_reps']].astype(float), test['calories_burned'])

# Printing the model score
print('Model score:', score)

# Creating a graph to show the user's progress over time
dates = pd.date_range(start='2023-01-01', end='2023-02-28', freq='D')
calories_burned = np.random.randint(500, 1000, size=len(dates))

plt.plot(dates, calories_burned)
plt.title('Calories Burned Over Time')
plt.xlabel('Date')
plt.ylabel('Calories Burned')
plt.show()
