import numpy as np
import matplotlib.pyplot as plt

# R_t = (S_t-S_{t-1}/S_{t-1})
#Returns R1,R2,R3...R 
#SD = volatility

path = "assignment1\meta_data\meta1y_daily.txt"

# Åpner filen med navnet 'filename.txt' i lesemodus ('r')
with open(path, 'r') as file:
    file.readline()
    price_open = []
    price_close = []
    for line in file:
        price_open.append(float(line.split(",")[1]))
        price_close.append(float(line.split(",")[5]))

daily_profit = []
trading_days = len(price_open)


for i in range(trading_days):
    daily_profit.append((price_close[i]-price_open[i])/price_open[i])

def expected_return(trading_days):
    return sum(daily_profit)/trading_days

u = expected_return(trading_days)

k = 0
for i in range(trading_days):
    k+= np.sqrt(((daily_profit[i]-u)**2)/trading_days)

print(k)

average_price = lambda price, days: sum(price)/days


[plt.scatter(i, price_close[i]) for i in range(trading_days)]
plt.show()


