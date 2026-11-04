import os
import sys
import argparse
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("EXCHANGERATE_API_KEY")

def fetch_exchange_rate(base_currency: str, target_currency: str) -> float:
    if not API_KEY or API_KEY == "your_actual_api_key_here":
        print("Error: EXCHANGERATE_API_KEY is missing or unconfigured in .env file.")
        print("Get a free API key at: https://www.exchangerate-api.com/")
        sys.exit(1)

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency.upper()}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data["result"] == "error":
            print(f"API Error: {data['error-type']}")
            sys.exit(1)
            
        rates = data.get("conversion_rates", {})
        target = target_currency.upper()
        
        if target not in rates:
            print(f"Error: Target currency '{target}' not found.")
            sys.exit(1)
            
        return rates[target]

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"Error: Base currency '{base_currency}' not found.")
        elif response.status_code == 401 or response.status_code == 403:
            print("Error: Invalid API Key. Please check your ExchangeRate-API key.")
        else:
            print(f"HTTP Error: {response.status_code}")
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
        sys.exit(1)

def display_conversion(amount: float, base: str, target: str, rate: float):
    converted_amount = amount * rate
    
    print("\n" + "=" * 40)
    print(" 💱 Currency Conversion Result")
    print("=" * 40)
    print(f" Rate       : 1 {base.upper()} = {rate:.4f} {target.upper()}")
    print(f" Conversion : {amount:.2f} {base.upper()} -> {converted_amount:.2f} {target.upper()}")
    print("=" * 40 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Convert an amount from one currency to another using live exchange rates.")
    parser.add_argument("amount", type=float, help="The amount of money to convert (e.g., 100 or 50.50)")
    parser.add_argument("base", type=str, help="The base currency code (e.g., USD, EUR, GBP)")
    parser.add_argument("target", type=str, help="The target currency code (e.g., JPY, CAD, AUD)")

    args = parser.parse_args()
    
    rate = fetch_exchange_rate(args.base, args.target)
    display_conversion(args.amount, args.base, args.target, rate)

if __name__ == "__main__":
    main()
