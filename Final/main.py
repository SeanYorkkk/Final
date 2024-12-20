import schedule
import time
from data_processing import  calculate_moving_average, highest_price, calculate_trend, calculate_volatility, predict_investment
from file_operations import load_from_file, save_to_file, fetch_live_stock_data


def update_data_automatically(filename, tickers):
    """
    Function to automatically fetch live stock data and update the file.
    """
    print("Fetching live stock data for:", ", ".join(tickers))
    fetch_live_stock_data(tickers, filename)
    print(f"Automated update completed for {filename}.")


def main():
    print("Welcome to the Stock Analysis Program!")
    stock_data = {}
    filename = "stocks.csv"
    tickers = ["AAPL", "MSFT", "GOOG","DOGE-USD","SMCI"]  # Set of tickers to fetch live data

    # Options menu
    while True:
        print("\nOptions:")
        print("1. Load stock data from a file")
        print("2. Analyze stock data")
        print("3. Predict investment potential")
        print("4. Save analysis to a file")
        print("5. Update stock data with live prices")
        print("6. Enable automatic updates (every 1 hour)")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Load stock data
            stock_data = load_from_file(filename)
            if stock_data:
                print(f"Loaded data: {stock_data}")
            else:
                print("No data loaded. Please check the file format.")

        elif choice == "2":
            # Analyze stock data
            if not stock_data:
                print("No stock data loaded. Please load data first.")
            else:
                ticker = input(f"Enter the ticker to analyze (available: {', '.join(stock_data.keys())}): ").strip().upper()
                if ticker in stock_data:
                    prices = stock_data[ticker]
                    ma = calculate_moving_average(prices, window_size=3)
                    print(f"3-Day Moving Average for {ticker}: {ma}")
                    print(f"Highest Price for {ticker}: {highest_price(prices)}")
                else:
                    print(f"Ticker {ticker} not found in loaded data.")

        elif choice == "3":
            # Predict investment potential
            if not stock_data:
                print("No stock data loaded. Please load data first.")
            else:
                ticker = input(
                    f"Enter the ticker to predict (available: {', '.join(stock_data.keys())}): "
                ).strip().upper()
                if ticker in stock_data:
                    prices = stock_data[ticker]
                    prediction = predict_investment(prices)
                    print(f"Prediction for {ticker}: {prediction}")
                else:
                    print(f"Ticker {ticker} not found in loaded data.")

        elif choice == "4":
            # Save raw stock data to a file
            if not stock_data:
                print("No stock data to save. Please load or analyze data first.")
            else:
                save_to_file(stock_data, "analysis.csv")
                print("Raw stock data saved to analysis.csv.")


        elif choice == "5":
            # Update stock data with live prices
            tickers = input(
                "Enter tickers (comma-separated, e.g., AAPL,MSFT,GOOG,DOGE-USD,SMCI): "
            ).strip().upper().split(",")
            fetch_live_stock_data(tickers, filename)

        elif choice == "6":
            # Enable automation
            print("Enabling automatic updates every 1 hour...")
            schedule.every(1).hour.do(update_data_automatically, filename, tickers)
            print("Press Ctrl+C to stop automatic updates.")
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nAutomatic updates stopped.")

        elif choice == "7":
            print("Exiting program.")
            break

       
if __name__ == "__main__":
     main()
    