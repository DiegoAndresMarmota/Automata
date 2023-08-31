import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read data from csv files
train = pd.read_csv('../Library/house_price/train.csv')
test = pd.read_csv('../Library/house_price/test.csv')

train.head(3)
train.columns

#Show the relationship between 'GrLivArea' and 'SalePrice'
train[['GrLivArea', 'SalePrice']].head()
train.plot.scatter(x='GrLivArea', y='SalePrice')
plt.show()

#Parametros de la recta
w = 100
b = 0

#Determinar la función linspace, a trves de la ecuación de la recta
x = np.linspace(0,train['GrLivArea'].max(),100)
y = w*x + b

#Graficar a través con un modelo de puntos, una linea roja 'r', determinando un máximo porciento del 10% de 'Y'.
train.plot.scatter(x='GrLivArea', y='SalePrice')
plt.plot(x, y, c = 'r')
plt.ylim(0, train['SalePrice'].max()*1.1)
plt.show()

#Calcular la diferencia entre 'Pred' y 'SalePrice' con el valor de 'Pred'
train['pred'] = train['GrLivArea']*w+b
train['diff'] = train['pred']-train['SalePrice']
train['cuad'] = train['diff']**2
train.head()

#Calcular el error cuadratico medio de 'cuad'
train['cuad'].mean()

#Calcular el error cuadratico medio de 'cuad' para cada valor de 'w'
w = np.linspace(50,200,50)
grid_error = pd.DataFrame(w, columns=['w'])
grid_error.head()

#Determinar las diferencias con sum_error, a través de w
def sum_error(w, train):
    b=0
    train['pred'] = train['GrLivArea']*w+b
    train['diff'] = train['pred']-train['SalePrice']
    train['cuad'] = train['diff']**2
    return train['cuad'].mean()

grid_error['error'] = grid_error['w'].apply(lambda w: sum_error(w, train))
grid_error.head()

grid_error.plot(x='w', y='error')
plt.show()