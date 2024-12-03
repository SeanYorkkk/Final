import numpy as np
from scipy.stats import linregress


def calculate_moving_average(prices, window_size):
    """Calculate moving averages for the given prices."""
    if len(prices) < window_size:
        return []
    return [sum(prices[i:i+window_size]) / window_size for i in range(len(prices) - window_size + 1)]


def highest_price(prices):
    """Find the highest price in the list."""
    return max(prices)


def calculate_trend(prices):
    """Calculate the trend of stock prices using linear regression."""
    x = np.arange(len(prices))  # Time as an independent variable
    slope, _, _, _, _ = linregress(x, prices)
    return slope


def calculate_volatility(prices):
    """Calculate the volatility (standard deviation) of daily returns."""
    returns = np.diff(prices) / prices[:-1]  # Daily returns
    volatility = np.std(returns)  # Standard deviation of returns
    return volatility


def predict_investment(prices, trend_threshold=0.01, volatility_threshold=0.02):
    """
    Predict whether the stock will grow or crash, and if it's a good investment.
    Returns a string recommendation based on trend and volatility.
    """
    slope = calculate_trend(prices)  # Trend of prices
    volatility = calculate_volatility(prices)  # Risk level based on price fluctuations

    # Evaluate based on slope and volatility
    if slope > trend_threshold and volatility < volatility_threshold:
        return "The stock is likely to grow and is a low-risk investment."
    elif slope > trend_threshold and volatility >= volatility_threshold:
        return "The stock is likely to grow but has higher risk due to volatility."
    elif slope < -trend_threshold:
        return "The stock is likely to decline. Not a good investment."
    elif abs(slope) <= trend_threshold and volatility < volatility_threshold:
        return "The stock is stable and low-risk, but lacks strong growth potential."
    else:
        return "The stock is stable but has higher risk due to volatility."
