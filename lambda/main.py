from calc import return_five
from spy_price import get_spy_price

def handler(event, context):
    num = return_five()
    current_stock_price = get_spy_price()

    return f'Hello Avneet, from Lamda - the current SPY stock price is > {current_stock_price}'
