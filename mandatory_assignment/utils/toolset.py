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

def gaussian_curve(x, volatility, mean):
    return (1/(np.sqrt(2*np.pi*volatility**2)))*np.exp(-((x-mean)**2)/(2*volatility**2))

def plot_histogram(Portfolio, x):
    return None

def plot_time_series(Portfolio):
    
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

    for stock in [s for s in Portfolio if "daily" in s]:
        axes[0].plot(Portfolio[stock]["returns"], label=f'{stock} Returns')
        axes[0].set_title('Daily Returns')
        axes[0].set_xlabel('Trading Days')
        axes[0].set_ylabel('Returns')
        axes[0].legend()
        axes[0].grid(True)

    # Plotting weekly returns
    for stock in [s for s in Portfolio if "weekly" in s]:
        axes[1].plot(Portfolio[stock]["returns"], label=f'{stock} Returns')
        axes[1].set_title('Weekly Returns')
        axes[1].set_xlabel('Trading Weeks')
        axes[1].set_ylabel('Returns')
        axes[1].legend()
        axes[1].grid(True)

    plt.tight_layout()  # Adjusts the spaces between the plots
    plt.show()

if __name__ == "__main__":
    None