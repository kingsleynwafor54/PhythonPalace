import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# %matplotlib inline
df=pd.read_csv("C:\\Users\\USCHIP\\Downloads\\weather.csv")
print(df)
print(df.shape)
print(df.describe())
df.plot(x='MinTemp', y='MaxTemp',style='o')
plt.title('MinTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(df['MaxTemp'])
plt.show()
#Data splicing
x=df['MinTemp'].values.reshape(-1,1)
y=df['MaxTemp'].values.reshape(-1,1)

x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

regressor=LinearRegression()
# training the algorithm
regressor.fit(x_train, y_train)
print('Intercept:',regressor.intercept_)
print('Coefficient',regressor.coef_)
y_pred=regressor.predict(x_test)

dff=pd.DataFrame({'Actual':y_test.flatten(),'Predicated':y_pred.flatten()})
print(dff)