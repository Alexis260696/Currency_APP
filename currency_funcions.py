def get_price_MXN(response, currency):
    
    date = response["time_last_update_utc"]
    currency = currency
    bc = "MXN"
    price_MXN = response["conversion_rates"][bc]
    
    
    return date, currency, bc, price_MXN
