import numpy as np
from scipy.optimize import minimize

# Given data
E = np.array([0.001804765944968264, 0.0018757223194177802, 0.0021054474320001946])  # Expected returns
Sigma = np.array([
    [0.00137138, 0.00106065, 0.00187121],
    [0.00106065, 0.00279301, 0.00218395],
    [0.00187121, 0.00218395, 0.00783026]
])  # 3x3 Covariance Matrix subset

# The value for r0 isn't provided directly. For now, let's assume it to be zero.
# If you have a specific value for r0, replace the below value.
r0 = 0

# Objective function: Negative Sharpe Ratio (since we want to maximize Sharpe, but the minimize function minimizes)
def negative_sharpe(x):
    portfolio_return = np.dot(E, x)
    portfolio_volatility = np.sqrt(np.dot(x.T, np.dot(Sigma, x)))
    sharpe = (portfolio_return - r0) / portfolio_volatility
    return -sharpe

# Constraints
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # The weights sum up to 1

# Bounds for weights (assuming no short-selling is allowed, i.e., weights between 0 and 1)
bounds = [(0, 1) for asset in range(len(E))]

# Initial guess (evenly distributed for simplicity)
init_guess = [1./len(E) for asset in E]

# Run the optimizer
solution = minimize(negative_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Extract the weights of the tangent portfolio
x_T = solution.x

print("Optimal weights for the tangent portfolio:", x_T)
