import pandas as pd
import arrow
import json
import requests
from alpha_vantage.timeseries import TimeSeries

app = TimeSeries('S4619YJ6YDGFXD17')

ticker = input("Enter ticker symbol: ")    #getting the ticker symbol from the user
timeframes = ['1m', '5m', '30m', '60m']

def get_ohlc_data(ticker, timeframes):
    ohlc_data = []
    for timeframe in timeframes:
        try:
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
            r = requests.get(url)
            data = r.json()

            print(data)     
            data, meta_data = app.get_intraday(symbol=ticker,interval=timeframe, outputsize='full')
            df = pd.DataFrame(data)
            df.reset_index(level=0, inplace=True)
            df = df.rename(columns={'index': 'Datetime', '1. open': 'OPEN', '2. high': 'HIGH', '3. low': 'LOW', '4. close': 'CLOSE', '5. volume': 'VOLUME'})
            df['TICKER'] = ticker
            ohlc_data.append(df)
        except Exception as e:
            print(f"Error: {e}")
    return ohlc_data

data = get_ohlc_data(ticker, timeframes)
for df in data:
    print(df)
