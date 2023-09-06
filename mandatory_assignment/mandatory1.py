import numpy as np
import matplotlib.pyplot as plt
from utils.readfiles import calculate_returns, readfile, calculate_mean, calculate_volatility


Path = {
    "RACE_daily" : "mandatory_assignment\companies\RACE_daily.txt",
    "RACE_weekly" : "mandatory_assignment\companies\RACE_weekly.txt",
    "AMZN_daily": "mandatory_assignment\companies\AMZN_daily.txt",
    "AMZN_weekly": "mandatory_assignment\companies\AMZN_weekly.txt",
}

Companies = {
    "RACE_daily" : {
        "close": [],
        "trading_days": int,
        "returns" : [],
        "mean" : float,
        "volatility" : float,
    },
    "RACE_weekly" : {
        "close" : [],
        "trading_days": int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
    },
    "AMZN_daily" : {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
    },
    "AMZN_weekly": {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
    }
}


for stock in Companies:
    Companies[stock]["close"], Companies[stock]["trading_days"] = readfile(Path[stock]) 
    Companies[stock]["returns"] = calculate_returns(Companies[stock]["close"], Companies[stock]["trading_days"])
    Companies[stock]["mean"] = calculate_mean(Companies[stock]["returns"], Companies[stock]["trading_days"])
    Companies[stock]["volatility"] = calculate_volatility(Companies[stock]["returns"], Companies[stock]["trading_days"])

for stock in Companies:
    print(Companies[stock]["volatility"], Companies[stock]["mean"])



def hvisdubryrdeg():
    plt.figure(figsize=(12, 6))
    for stock in Companies:
        if "daily" in stock:
            plt.plot(Companies[stock]["returns"], label=f'{stock} daily returns')
            plt.legend()
        elif "weekly" in stock:
            plt.plot(Companies[stock]["returns"], label=f'{stock} weekly returns')
            plt.xlabel('Time')
            plt.ylabel('Returns')
            plt.legend()
    plt.show()