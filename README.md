# 🌍 Currency Rates to MongoDB

> **Fetch live currency rates and store them in MongoDB**

---

## 🔧 Prerequisites

* **Python 3.7+**
* **pip** packages:

  * `currencyapicom`
  * `pymongo`
* **MongoDB URI** (set as `MONGO_URI` environment variable)
* **CurrencyAPI.com API Key** (set as `CURRENCY_API_KEY` environment variable)

---

## 🚀 Quick Start

1. **Install dependencies**

   ```bash
   pip install currencyapicom pymongo
   ```

2. **Set environment variables**

   ```bash
   export MONGO_URI="mongodb://<username>:<password>@host:27017/"
   export CURRENCY_API_KEY="your_api_key_here"
   ```

3. **Run the script**

   ```bash
   python update_rates.py
   ```

   * The script will:

     1. Fetch latest rates for USD, KES, UGX, TZS, RWF, ETB, NGN, GHS, ZAR, EGP, AED, BTC, ETH
     2. Connect to MongoDB using `MONGO_URI`
     3. Upsert each currency’s rate in the `currencyExchangeRates.rates` collection

---

## 🔍 How It Works

* **`currencyapicom.Client`** uses your API key to fetch live exchange rates.
* A dictionary maps each currency code to its latest rate data.
* **`pymongo.MongoClient`** connects to your MongoDB instance.
* For each currency, the script runs an **`update_one`** with `upsert=True` to insert or update the document:

  ```json
  {
    "_id": "USD",
    "value": { ...rate data... }
  }
  ```

---

## ❤️ Enjoy!

A lightweight solution to keep your MongoDB collection in sync with live currency rates. Feel free to add more currencies or schedule it with a cron job!
