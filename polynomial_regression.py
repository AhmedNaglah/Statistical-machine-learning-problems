import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import random
from sklearn.metrics import mean_squared_error as mse


f, n = map(int,input().split())

x=[ None for k in range(n)]
y=[ None for k in range(n)]

for i in range(n):
    *x[i], y[i] = map(float,input().split())

n_test = int(input())

x_test=[]
for i in range(n_test):
    inp = list(map(float, input().split()))
    x_test.append(inp)

#estimate order of polynomial , let's try linear regression, second order, third, forth and fifth 
#split data into training and validation
#sklean split

x_train, x_val, y_train, y_val = train_test_split(x,y, test_size=0.3, random_state=42 )

lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict(x_val)
score = mse(y_val, y_pred)
scores = [score]
for i in range(2,6,1):
    poly = PolynomialFeatures(degree=i)
    x_train_ = poly.fit_transform(x_train)
    x_val_ = poly.fit_transform(x_val)
    lr.fit(x_train_,y_train)
    y_pred = lr.predict(x_val_)
    score = mse(y_val, y_pred)
    scores.append(score)

midx = scores.index(min(scores)) 

#Now we have the optimum order
order = midx+1
poly = PolynomialFeatures(degree=order)
x_ = poly.fit_transform(x)
x_test_ = poly.fit_transform(x_test)
lr.fit(x_,y)
y_pred = lr.predict(x_test_)
y_pred = list(y_pred)
for i in range(len(y_pred)):
    print(str(round(y_pred[i],2)))
