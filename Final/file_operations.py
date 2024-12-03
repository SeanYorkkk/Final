import csv
import yfinance as yf


def load_from_file(filename):
    """
    Load stock data from a CSV file.
    Expected CSV format:
    Ticker,Price1,Price2,Price3,...
    """
    data = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 1:  # Ensure the row has data
                    ticker = row[0]
                    prices = list(map(float, row[1:]))
                    data[ticker] = prices
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except ValueError:
        print(f"Error: Invalid data format in file {filename}.")
    return data


def save_to_file(data, filename):
    """
    Save stock data (raw information) to a CSV file.
    :param data: Dictionary containing tickers and their prices.
    :param filename: The name of the file to save the data.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Prices"])  # Header row
        for ticker, prices in data.items():
            writer.writerow([ticker] + prices)
    print(f"Data saved to {filename}.")



def fetch_live_stock_data(tickers, filename):
    """
    Fetch live stock data for the given tickers and update the CSV file.
    """
    stock_data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            history = stock.history(period="1d", interval="1m")  # 1-minute intervals
            prices = history["Close"].tolist()  # Get closing prices
            stock_data[ticker] = prices[-10:]  # Keep the last 10 prices
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    # Write updated stock data to the CSV file
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for ticker, prices in stock_data.items():
            writer.writerow([ticker] + prices)
    print(f"Updated stock data saved to {filename}.")
