from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        # Get the exchange rate
        rate = c.get_rate(from_currency, to_currency)

        # Perform the conversion
        converted_amount = amount * rate

        # Print the result
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage: convert 100 USD to EUR
    amount_to_convert = float(input("Enter the amount to convert: "))
    from_currency_code = input("Enter the source currency code: ").upper()
    to_currency_code = input("Enter the target currency code: ").upper()

    convert_currency(amount_to_convert, from_currency_code, to_currency_code)
