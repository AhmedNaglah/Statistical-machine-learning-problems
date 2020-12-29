from sklearn.linear_model import LinearRegression
import math
import numpy as np

def printActions(actions):
    n=len(actions)
    print(n)
    if n==0:
        pass
    else:
        for i in range(n):
            print(actions[i]['name'] + ' ' + actions[i]['decision']+ ' ' + str(actions[i]['qty']))

def predictNextDayPrice(history):
    y= history
    n = len(y)
    x= [ [k**2] for k in range(1,n+1,1)]
    lr = LinearRegression()
    lr.fit(x,y)
    return lr.predict([[n**2]])[0]

def decideSell(stocks, m, k):
    pass
    n=len(stocks)
    actions = []
    k_new = k
    for i in range(n):
        stock = stocks[i]
        if stock['qty']>0:
            y = stock['history']
            y_current = y[-1]
            y_predicted = predictNextDayPrice(y)
            loss = y_current-y_predicted
            if loss>0:
                #print(stock['name'])
                #print(loss)
                qty = min(stock['qty'],k)
                actions.append({'name': stock['name'], 'decision':'SELL', 'qty': stock['qty']})
                k_new -= qty
    return actions, k_new
            
def decideBuy(stocks, m, k):
    pass
    n=len(stocks)
    profits = []
    for i in range(n):
        stock = stocks[i]
        y = stock['history']
        y_current = y[-1]
        y_predicted = predictNextDayPrice(y)
        profit = y_predicted-y_current
        profits.append(profit)
    idxs = np.argsort(profits)
    #print(idxs)
    for i in range(n):
        idx = idxs[n-i-1]
        stock = stocks[idx]
        #print('id :' + str(idx))
        #print('name :' + stock['name'])
        price = stock['history'][-1]
        #print('price :' + str(price))
        if price<=m:
            qty = math.floor(m/price)
            qty = min(k, qty)
            #print('Stock is selected to buy:')
            #print(stock['name'])
            #print(qty)
            if qty>0:
                actions = [{'name': stock['name'], 'decision':'BUY', 'qty': qty}]
                return actions
    return []

meta = input().split()
m = float(meta[0]); k=int(meta[1]); d=int(meta[2])

#print(m)
#print(k)
#print(d)

stocks = []
for i in range(k):
    stck = input().split()
    stocks.append({'name': stck[0], 'qty': int(stck[1]), 'history': list(map(float,stck[2:]))})
#print(stocks)

if d==0:
    actions = []
    for i in range(k):
        stock = stocks[i]
        if stock['qty']>0:
            actions.append({'name': stock['name'], 'decision':'SELL', 'qty': stock['qty']})
    printActions(actions)
else:
    actionsSELL, k_new = decideSell(stocks, m, k)
    actionsBUY = decideBuy(stocks, m, k_new)
    #print(actionsSELL)
    #print(actionsBUY)
    actionsSELL.extend(actionsBUY)
    allactions = actionsSELL
    #print(allactions)
    printActions(allactions)
