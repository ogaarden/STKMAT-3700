import numpy as np
import matplotlib.pyplot as plt
from utils.toolset import calculate_returns, readfile, calculate_mean, calculate_volatility, gaussian_curve, plot_time_series


Path = {
    "RACE_daily" : "mandatory_assignment\stock_data\RACE_daily.txt",
    "RACE_weekly" : "mandatory_assignment\stock_data\RACE_weekly.txt",
    "AMZN_daily": "mandatory_assignment\stock_data\AMZN_daily.txt",
    "AMZN_weekly": "mandatory_assignment\stock_data\AMZN_weekly.txt",
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

plot_time_series(Companies)


x = np.linspace(min(Companies["AMZN_weekly"]["returns"]), max(Companies["AMZN_weekly"]["returns"]), 100)

y = gaussian_curve(x, (Companies["AMZN_weekly"]["volatility"]), Companies["AMZN_weekly"]["mean"])


plt.subplot(1, 2, 1)
plt.hist(Companies["AMZN_weekly"]["returns"], bins=50, density=True, alpha=0.6, color='g')  # Histogram of daily returns
plt.plot(x, y, linewidth=2, color='r')  # Gaussian curve
plt.title('Daily Returns and Fitted Gaussian Curve')
plt.xlabel('Daily Return')
plt.ylabel('Density')
plt.savefig("Histogram of returns")