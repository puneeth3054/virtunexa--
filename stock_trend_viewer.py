import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import logging
import os

# === Logging Setup ===
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/stock_trends.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Stock Fetching and Plotting ===
def fetch_and_plot_stock(ticker_symbol):
    try:
        logging.info(f"Fetching stock data for: {ticker_symbol}")
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="5d")

        if hist.empty:
            print("No data found. Please check the ticker symbol.")
            logging.warning(f"No data found for {ticker_symbol}")
            return

        print(hist[["Open", "Close"]])
        hist[["Open", "Close"]].plot(title=f"{ticker_symbol} - Last 5 Days")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        plt.show()

        logging.info(f"Displayed trend chart for: {ticker_symbol}")

    except Exception as e:
        print("An error occurred while fetching stock data.")
        logging.error(f"Error fetching data for {ticker_symbol}: {e}")

# === Console Interface ===
def main():
    print("=== Real-Time Stock Trend Viewer ===")
    while True:
        ticker = input("Enter stock ticker symbol (e.g., AAPL) or 'exit' to quit: ").strip().upper()
        if ticker == "EXIT":
            print("Exiting program.")
            break
        elif ticker:
            fetch_and_plot_stock(ticker)
        else:
            print("Please enter a valid ticker.")

if __name__ == "__main__":
    main()
