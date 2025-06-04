import currencyapicom
from pymongo import MongoClient

mongodb_connections_url = '<MONGO_URI>'
currencyapi_apikey = "<CURRENCY_API_KEY>"
client = currencyapicom.Client(currencyapi_apikey)

collected_currencies_dict = {
    'USD':client.latest(base_currency='USD'),
    'KES':client.latest(base_currency='KES'),
    'UGX':client.latest(base_currency='UGX'),
    'TZS':client.latest(base_currency='TZS'),
    'RWF':client.latest(base_currency='RWF'),
    'ETB':client.latest(base_currency='ETB'),
    'NGN':client.latest(base_currency='NGN'),
    'GHS':client.latest(base_currency='GHS'),    
    'ZAR':client.latest(base_currency='ZAR'),
    'EGP':client.latest(base_currency='EGP'),    
    'AED':client.latest(base_currency='AED'),
    'BTC':client.latest(base_currency='BTC'),      
    'ETH':client.latest(base_currency='ETH'),          
}
client = MongoClient(mongodb_connections_url)
db = client["currencyExchangeRates"]
collection = db["rates"]
for key, value in collected_currencies_dict.items():
    collection.update_one(
        {"_id": key},
        {"$set": {"value": value}},
        upsert=True
    )
