import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

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

def expected_return(r: list) -> float:
    s = 0
    T = len(r)
    for i in range(T):
        s += r[i]
    return s/T

def plot_histogram(Portfolio) -> None:
    for stock in Portfolio:
        x = np.linspace(min(Portfolio[stock]["returns"]), max(Portfolio[stock]["returns"]), 100)
        y = gaussian_curve(x, Portfolio[stock]["volatility"], Portfolio[stock]["mean"])
        plt.hist(Portfolio[stock]["returns"], bins=50, density=True, alpha=0.6, color='g')
        plt.plot(x, y, linewidth= 2, color = 'r')
        plt.show()

def plot_time_series(Portfolio) -> None:
    
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
    plt.savefig("Time series")
    plt.show()
    


def cov_matrix(portfolio, n):
    selected_keys = list(portfolio.keys())[:n*2]
    weekly_returns = [portfolio[stock]["returns"] for stock in selected_keys if "_weekly" in stock]
    if not weekly_returns:
        return None
    returns_matrix_weekly = np.transpose(weekly_returns)
    cov_matrix_weekly = np.cov(returns_matrix_weekly, rowvar=False)
    return cov_matrix_weekly

def objective(w, cov):
    return np.dot(w, np.dot(cov, w))

def optimize_min_variance(cov):
    num_assets = len(cov)
    
    # Initial guess for weights (equal weights)
    initial_weights = [1./num_assets for _ in range(num_assets)]
    
    # Constraints: sum of weights is 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    
    # Asset weights are bound between 0 and 1
    bounds = tuple((0, 1) for asset in range(num_assets))
    
    solution = minimize(objective, initial_weights, args=(cov,), method='SLSQP', bounds=bounds, constraints=constraints)
    
    return solution.fun, solution.x

def optimized_returns(portfolio, w, n):
    selected_keys = [key for key in list(portfolio.keys())[:n*2] if "_weekly" in key]
    total_return = 0
    # Ensure that the length of weights matches the number of selected assets
    assert len(w) == len(selected_keys), "Mismatch between number of weights and selected assets"
    for i, key in enumerate(selected_keys):
        total_return += expected_return(portfolio[key]["returns"]) * w[i]
        
    return total_return


if __name__ == "__main__":
    None