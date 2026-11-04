# CLI Currency Converter

A lightweight, command-line Python tool that fetches live exchange rates and converts money between different currencies using ExchangeRate-API.

## Windows & VS Code Setup Instructions

1. **Extract this folder** into your `Documents/Project` directory (e.g., `currency-converter`).
2. **Open the folder in VS Code**:
   - Open VS Code, click `File > Open Folder`, and select your new extracted folder.
3. **Open the Integrated Terminal** (`Terminal > New Terminal`).
4. **Set up your Python environment**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. **Configure your API Key**:
   - Go to [ExchangeRate-API](https://www.exchangerate-api.com/) and sign up for a free API key.
   - Open the `.env` file in VS Code.
   - Replace `your_actual_api_key_here` with your real API key.

## Usage
Run these commands in your VS Code terminal to convert currencies:
```cmd
# Convert 100 USD to EUR
python converter.py 100 USD EUR

# Convert 50.50 GBP to JPY
python converter.py 50.50 GBP JPY
```
