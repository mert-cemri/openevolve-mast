'''
Handles the currency conversion logic.
'''
import config
def convert(amount, source_currency, target_currency):
    exchange_rates = config.load_exchange_rates()
    # Check if the source and target currencies are valid
    if source_currency not in exchange_rates:
        raise ValueError(f"Invalid source currency code: {source_currency}")
    if target_currency not in exchange_rates:
        raise ValueError(f"Invalid target currency code: {target_currency}")
    # Assuming all exchange rates are relative to USD
    usd_rate = exchange_rates['USD']
    source_rate = exchange_rates[source_currency]
    target_rate = exchange_rates[target_currency]
    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / source_rate
    converted_amount = amount_in_usd * target_rate
    return converted_amount