import numpy as np
import matplotlib.pyplot as plt
import utils.toolset as ut
from scipy.optimize import minimize

Path = {
    "RACE_daily" : "mandatory_assignment\stock_data\RACE_daily.txt",
    "RACE_weekly" : "mandatory_assignment\stock_data\RACE_weekly.txt",
    "AMZN_daily": "mandatory_assignment\stock_data\AMZN_daily.txt",
    "AMZN_weekly": "mandatory_assignment\stock_data\AMZN_weekly.txt",
    "TSLA_daily" : "mandatory_assignment\stock_data\TSLA_daily.txt",
    "TSLA_weekly" : "mandatory_assignment\stock_data\TSLA_weekly.txt",
    "SNAP_daily" : "mandatory_assignment\stock_data\SNAP_daily.txt",
    "SNAP_weekly" : "mandatory_assignment\stock_data\SNAP_weekly.txt",
    "AAPL_daily" : "mandatory_assignment\stock_data\AAPL_daily.txt",
    "AAPL_weekly" : "mandatory_assignment\stock_data\AAPL_weekly.txt",
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
    "RACE_weekly" : {
        "close" : [],
        "trading_days": int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
    "AMZN_daily" : {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
    "AMZN_weekly": {
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
    "TSLA_weekly":{
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
    "SNAP_weekly": {
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
    "AAPL_weekly": {
        "close" : [],
        "trading_days" : int,
        "returns" : [], 
        "mean" : float,
        "volatility" : float,
        "e_return" : [],
    },
}


for stock in Companies:
    Companies[stock]["close"], Companies[stock]["trading_days"] = ut.readfile(Path[stock]) 
    Companies[stock]["returns"] = ut.calculate_returns(Companies[stock]["close"], Companies[stock]["trading_days"])
    Companies[stock]["mean"] = ut.calculate_mean(Companies[stock]["returns"], Companies[stock]["trading_days"])
    Companies[stock]["volatility"] = ut.calculate_volatility(Companies[stock]["returns"], Companies[stock]["trading_days"])
    Companies[stock]["e_return"] = ut.expected_return(Companies[stock]["returns"])
    #print(ut.expected_return(Companies[stock]["returns"]))
#for stock in Companies:
    #print(Companies[stock]["volatility"], Companies[stock]["mean"])

def print_cov_matrix(n):
    print(f' {n}x{n} covariance matrix \n : {ut.cov_matrix(Companies, n)}' )

n = 5

cov_matrices = [ut.cov_matrix(Companies, n) for n in range(3, 6)]
min_variances = []
optimal_weights_list = []

for cov_matrix in cov_matrices:
    min_var, opt_weights = ut.optimize_min_variance(cov_matrix)
    print(opt_weights)
    min_variances.append(min_var)
    optimal_weights_list.append(opt_weights)


expected_returns = [ut.optimized_returns(Companies, w, len(w)) for w in optimal_weights_list]


colors = ['red', 'blue', 'green']
markers = ['o', 's', 'D']  # o: circle, s: square, D: diamond
labels = ['3 assets', '4 assets', '5 assets']
"""
for i, (variance, ret) in enumerate(zip(min_variances, expected_returns)):
    plt.scatter(variance, ret, color=colors[i], marker=markers[i], label=labels[i])

plt.xlabel('Volatility (Min Variance)')
plt.ylabel('Expected Return')
plt.title('Expected Return vs. Volatility for Portfolios')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
"""

#print(optimized_ret)
#for i in range(3,6):
#    ut.print_cov_matrix(Companies, i)
#r_m = range(i,n)xi ri

#ut.plot_time_series(Companies) # Oppgave b

ut.plot_histogram(Companies)


#stock_returns = [Companies[stock]['e_return'] for stock in list(Companies.keys())[::2]]
