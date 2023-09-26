import numpy as np
from scipy.stats import norm
import utils.toolset as ut
import matplotlib.pyplot as plt

import numpy as np
from scipy.stats import norm
import utils.toolset as ut
import matplotlib.pyplot as plt

Path = {
    "RACE_daily" : "mandatory_assignment\stock_data\RACE_daily.txt",
    "AMZN_daily": "mandatory_assignment\stock_data\AMZN_daily.txt",
    "TSLA_daily" : "mandatory_assignment\stock_data\TSLA_daily.txt",
    "SNAP_daily" : "mandatory_assignment\stock_data\SNAP_daily.txt",
    "AAPL_daily" : "mandatory_assignment\stock_data\AAPL_daily.txt",
}

Companies = {
    "RACE_daily" : {
        "close": [],
        "trading_days": int,
        "returns" : [],
        "mean" : float,
        "volatility" : float,
        "e_return" : []
    },
    "AMZN_daily" : {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
    "TSLA_daily": {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
    "SNAP_daily": {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
    "AAPL_daily": {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
}

K = [50, 60, 105, 110, 140, 145]
S = 174.8 # Price of apple

RRrate = 4.49 # percet
#K = strike price
#S = stock price
def black_scholes_for_calls(K, S, T, r, sigma) -> float :
    """
    Parameters:
        K = Strike price of call option
        S = Current stock price
        T = Time from t = 0 to expiry date
        r = Risk free return
        sigma = volatility
    Returns: 
        The value of the call option C
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    C = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    return C

T = [1/12, 3/12] # 1 month, specific for 3a
r = 0.045 # Current risk free interest rate

for stock in Companies:
    Companies[stock]["close"], Companies[stock]["trading_days"] = ut.readfile(Path[stock]) 
    Companies[stock]["returns"] = ut.calculate_returns(Companies[stock]["close"], Companies[stock]["trading_days"])
    Companies[stock]["mean"] = ut.calculate_mean(Companies[stock]["returns"], Companies[stock]["trading_days"])
    Companies[stock]["volatility"] = ut.calculate_volatility(Companies[stock]["returns"], Companies[stock]["trading_days"])*np.sqrt(250)



call_opt_prices = {
    "month" : [],
    "3month" : [],
}


for i , stock in enumerate(Companies):
    sigma = Companies[stock]["volatility"]
    for b, j, timescale in enumerate(call_opt_prices):
        call_opt_prices[timescale].append(black_scholes_for_calls(K[i], S, T[j], r, sigma))

print(call_opt_prices["month"], call_opt_prices["3month"])

""" Oppgave a
for stock in Companies:
    K, S, sigma = 4900, 5000, Companies[stock]["volatility"]
    print(f"Company: {stock}, Time: {T[0]}")
    print(black_scholes_for_calls(K, S, T[0], r, sigma))
    print(black_scholes_for_calls(K, S, T[1], r, sigma))
"""