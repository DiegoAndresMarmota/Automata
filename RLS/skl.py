from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

#Read data from csv files
train = pd.read_csv('../Library/house_price/train.csv')
test = pd.read_csv('../Library/house_price/test.csv')

#Definit el input y el output
x_train = np.array(train['GrLivArea']).reshape((-1,1))
y_train = np.array(train['SalePrice'])

#Creación del modelo
model = LinearRegression(fit_intercept=False)
model.fit(x_train,y_train)

#Mostrar los resultados
print(f"intercepto (b): {model.intercept_}")
print(f"pendiente (w): {model.coef_}")

"""
intercepto (b): 0.0
pendiente (w): [118.06909986]
"""