def authenticate_user():
    user_id = input("Enter user ID: ")
    password = input("Enter password: ")
    if user_id == "ritish" and password == "ritish":
        return True
    else:
        return False

def get_crypto_prices(symbols, years):
    # Simulated historical data for cryptocurrencies
    historical_data = {
        "BTC": {"2010": 0.08, "2014": 340, "2018": 13000, "2022": 47000, "2024": 40000},
        "ETH": {"2014": 300, "2018": 200, "2022": 3000, "2024": 2500},
        "SOL": {"2018": 1.5, "2022": 33, "2024": 100},
        "BNB": {"2018": 10, "2022": 410, "2024": 300},
        "DOGE": {"2014": 0.00026, "2018": 0.006, "2022": 0.08, "2024": 0.2},
        "SHIB": {"2022": 0.00002, "2024": 0.00003},
        "USDC": {"2018": 1, "2022": 1, "2024": 1},
        "BCH": {"2018": 1500, "2022": 600, "2024": 300},
        "LTC": {"2014": 10, "2018": 50, "2022": 100, "2024": 130}
    }

    # Retrieve the historical prices for the requested years
    result = {}
    for symbol in symbols:
        result[symbol] = {}
        for year in years:
            result[symbol][year] = historical_data.get(symbol, {}).get(year, 'N/A')  # Default to 'N/A' if data is missing
    return result

def display_crypto_data(prices):
    # Prints the prices in a formatted way
    for symbol, data in prices.items():
        print(f"--- {symbol} Historical Prices ---")
        for year, price in data.items():
            print(f"{year}: ${price}")

def main():
    # Prompt for user authentication
    if not authenticate_user():
        print("Invalid user ID or password.")
        return
    
    # List of cryptocurrencies and years we want to track
    crypto_symbols = ["BTC", "ETH", "SOL", "BNB", "DOGE", "SHIB", "USDC", "BCH", "LTC"]
    years = ["2010", "2014", "2018", "2022", "2024"]

    # Fetch the historical prices
    historical_prices = get_crypto_prices(crypto_symbols, years)

    # Display the historical prices
    display_crypto_data(historical_prices)

main()
