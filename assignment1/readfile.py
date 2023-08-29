import numpy as np
import matplotlib.pyplot as plt

path = "assignment1/meta_data/meta1y_daily.txt"

with open(path, 'r') as file:
    file.readline()
    price_close = []
    for line in file:
        price_close.append(float(line.split(",")[5]))

trading_days = len(price_close)

# Calculating daily returns, R = R_t+1 - R_t / R_t
daily_returns = [(price_close[i + 1] - price_close[i]) / price_close[i] for i in range(trading_days - 1)]

# Calculating expected return (mean)
u = sum(daily_returns) / trading_days

# Calculating volatility (standard deviation)
k = np.sqrt(sum([(r - u)**2 for r in daily_returns]) / trading_days)
x = np.linspace(0,trading_days,trading_days)

def gaussian_curve(x, k, u):
    return (1/(np.sqrt(2*np.pi*k*k)))*np.exp(-((x-u)**2)/(2*k*k))

x = np.linspace(min(daily_returns), max(daily_returns), 100)  # Choose a relevant scale
y = gaussian_curve(x, k, u)

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(daily_returns, bins=50, density=True, alpha=0.6, color='g')  # Histogram of daily returns
plt.plot(x, y, linewidth=2, color='r')  # Gaussian curve
plt.title('Daily Returns and Fitted Gaussian Curve')
plt.xlabel('Daily Return')
plt.ylabel('Density')
plt.show()