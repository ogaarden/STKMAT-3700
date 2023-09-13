import numpy as np
import matplotlib.pyplot as plt

path ={
    "weekly" : "meta_data/meta1y_daily.txt",
    "daily" : "meta_data/meta2y_weekly.txt",
}


with open(path["weekly"], 'r') as file:
    file.readline()
    price_close_w = []
    for line in file:
        price_close_w.append(float(line.split(",")[5]))

with open(path["daily], 'r') as file:
    file.readline()
    price_close = []
    for line in file:
        price_close.append(float(line.split(",")[5]))

trading_days = len(price_close)
trading_days_w = len(price_close_w)

# Calculating daily returns, R = R_t+1 - R_t / R_t
daily_returns = [(price_close[i + 1] - price_close[i]) / price_close[i] for i in range(trading_days - 1)]
weekly_returns = [(price_close_w[i + 1] - price_close_w[i]) / price_close_w[i] for i in range(trading_days_w - 1)]
              
# Calculating expected return (mean)
u = sum(daily_returns) / trading_days
uw = sum(weekly_returns) / trading_days_w

# Calculating volatility (standard deviation)
k = np.sqrt(sum([(r - u)**2 for r in daily_returns]) / trading_days)
kw = np.sqrt(sum([(r - u)**2 for r in weekly_returns]) / trading_days_w)

def gaussian_curve(x, k, u):
    return (1/(np.sqrt(2*np.pi*k*k)))*np.exp(-((x-u)**2)/(2*k*k))

x = np.linspace(min(daily_returns), max(daily_returns), 100)  # Choose a relevant scale
y = gaussian_curve(x, k, u)
yw = gaussian_curve(x,kw,uw)

print(f"D,W: expected returns: {u, uw} volatility: {k, kw}")

#Covariance matrix



# Plotting
# Create the figure
plt.figure(figsize=(20, 6))  # Adjust the size to fit the subplots

# First subplot: Duplicate of the original plot
plt.subplot(1, 2, 1)
plt.hist(daily_returns, bins=50, density=True, alpha=0.6, color='g')  # Histogram of daily returns
plt.plot(x, y, linewidth=2, color='r')  # Gaussian curve
plt.title('Daily Returns and Fitted Gaussian Curve')
plt.xlabel('Daily Return')
plt.ylabel('Density')

# Second subplot: Duplicate of the original plot
plt.subplot(1, 2, 2)
plt.hist(weekly_returns, bins=50, density=True, alpha=0.6, color='g')  # Histogram of daily returns
plt.plot(x, y, linewidth=2, color='r')  # Gaussian curve
plt.title('Weekly Returns and Fitted Gaussian Curve')
plt.xlabel('Weekly return')
plt.ylabel('Density')
plt.savefig("Histogram of returns")
# Show the plots
plt.show()


