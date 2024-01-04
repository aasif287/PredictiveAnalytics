#loads the necessary librarys 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
#reads the data file and seperates the columns 
data = pd.read_csv("avocado-production-data.csv",sep="\t")
#plots the data in a line plot (without labels 
plt.plot(data['year'],data['production'])
#creates data frame from csv and seperates data of X and Y axis
df = pd.DataFrame(data)
x = df['year'].values.reshape(-1, 1)
y=df['production']
#creates linear regression model and puts the data points in model and predicts future models 
model = LinearRegression()
model.fit(x, y)
avocado_pred = model.predict(x)
#plots previous line plot with regression line in red with labels 
plt.plot(data['year'],data['production'])
plt.plot(x, avocado_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Avocado Production By Year With Linear Regression')
plt.xlabel('Year')
plt.ylabel('Amount of Production (in Millions)')
#puts the value 2022 in an array to be placed in the prediction model
z = np.array([[2022]]) 
predict = model.predict(z)
# Prints value
print(f"The amount of avocado prouduction in 2022 is {predict[0]} Million Tons ")