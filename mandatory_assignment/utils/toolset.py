import numpy as np
import matplotlib.pyplot as plt

def readfile(filename):
    close = []
    with open (filename, "r") as file:
        file.readline()
        for line in file:
            close.append(float(line.split(",")[4]))
    return close, len(close)

def calculate_returns(price, trading_days):
    returns = []
    for i in range(trading_days-1):
        returns.append((price[i+1]-price[i])/price[i])
    return returns


def calculate_mean(returns, trading_days):
    return sum(returns)/trading_days

def calculate_volatility(returns, trading_days):
    u = calculate_mean(returns, trading_days)
    return np.sqrt(sum([(r - u)**2 for r in returns]) / trading_days)



if __name__ == "__main__":
    None