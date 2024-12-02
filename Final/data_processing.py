def calculate_moving_average(prices, window_size):
    if len(prices) < window_size:
        return []
    return [sum(prices[i:i+window_size]) / window_size for i in range(len(prices) - window_size + 1)]

def highest_price(prices):
    return max(prices)


def lowest_price(prices):
    """Find the lowest price in the list."""
    return min(prices)
