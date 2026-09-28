import requests
import sys
amount = sys.argv[1]
try:
    amount = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=901f4ca080ab4433101a3bc265ee76cb811ea2857560c4ac2d9f0ce7f48882de")
    response.raise_for_status()
except requests.RequestException:
    sys.exit("Connection Error")
except ValueError:
    sys.exit("Not a number")
content = response.json()
currency = content['data']['priceUsd']
print(f"${float(currency) * amount:,.4f}")
