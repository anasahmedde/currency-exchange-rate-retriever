import currencyapicom
from pymongo import MongoClient
from datetime import datetime, timedelta

mongodb_connections_url = '<MONGO_URI>'
currencyapi_apikey = "<CURRENCY_API_KEY>"
client = currencyapicom.Client(currencyapi_apikey)
today = datetime.today()
yesterday_date = today - timedelta(days=1)
yesterday_date.strftime("%Y-%m-%d")  

collected_currencies_dict = {
    'USD':client.historical(yesterday_date, base_currency='USD'),
    'KES':client.historical(yesterday_date, base_currency='KES'),
    'UGX':client.historical(yesterday_date, base_currency='UGX'),
    'TZS':client.historical(yesterday_date, base_currency='TZS'),
    'RWF':client.historical(yesterday_date, base_currency='RWF'),
    'ETB':client.historical(yesterday_date, base_currency='ETB'),
    'NGN':client.historical(yesterday_date, base_currency='NGN'),
    'GHS':client.historical(yesterday_date, base_currency='GHS'),    
    'ZAR':client.historical(yesterday_date, base_currency='ZAR'),
    'EGP':client.historical(yesterday_date, base_currency='EGP'),    
    'AED':client.historical(yesterday_date, base_currency='AED'),
    'BTC':client.historical(yesterday_date, base_currency='BTC'),      
    'ETH':client.historical(yesterday_date, base_currency='ETH'),          
}

final_data = {f"{str(yesterday_date.date())}":collected_currencies_dict}
client = MongoClient(mongodb_connections_url)
db = client["currencyExchangeRates"]
collection = db["historicalRates"]
for key, value in final_data.items():
    collection.update_one(
        {"_id": key},
        {"$set": {"value": value}},
        upsert=True
    )
