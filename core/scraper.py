import requests

headers = {"User-Agent": "Mozilla/5.0"}

def get_nse_data(symbol):
    try:
        url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)

        data = session.get(url, headers=headers).json()

        info = data["info"]
        stats = data["metadata"]

        return {
            "symbol": symbol,
            "price": stats.get("lastPrice", 0),
            "pe": stats.get("pE", 25),
            "pb": stats.get("pb", 3),
            "market_cap": stats.get("marketCap", 0),
        }

    except:
        return None