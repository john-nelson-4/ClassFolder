url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=EYJDZ6HFWO4REUT1o'
r = requests.get(url)
data = r.json()

print(data)