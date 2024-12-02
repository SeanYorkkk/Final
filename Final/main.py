from data_processing import calculate_moving_average, highest_price
from file_operations import load_from_file, save_to_file

def main():
    print("Welcome to the Stock Analysis Program!")
    
    while True:
        print("\nOptions:")
        print("1. Load stock data from a file")
        print("2. Analyze stock data")
        print("3. Save analysis to a file")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            filename = input("Enter filename to load stock data (e.g., stocks.csv): ").strip()
            data = load_from_file(filename)
            print(f"Loaded data: {data}")
        elif choice == "2":
            prices = [float(price) for price in input("Enter stock prices (comma-separated): ").split(",")]
            ma = calculate_moving_average(prices, window_size=3)
            print(f"3-Day Moving Average: {ma}")
            print(f"Highest Price: {highest_price(prices)}")
        elif choice == "3":
            filename = input("Enter filename to save analysis: ").strip()
            data = {"Example Analysis": [100, 102, 105]}  # Replace with actual data
            save_to_file(data, filename)
            print(f"Data saved to {filename}.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    main()
