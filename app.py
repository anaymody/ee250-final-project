import requests
import json

# Alpha Vantage API: https://www.alphavantage.co/documentation/
AV_KEY = "UKRTY6HAA7CAQMNO"

SYMBOL = "IBM"

def my_app():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + SYMBOL + '&apikey=' + AV_KEY
    r = requests.get(url)    

    if r.status_code == 200: # Status: OK
        data = r.json()


        date = data["Meta Data"]["3. Last Refreshed"]
        information = data["Time Series (Daily)"][date]
        
        day_open = information["1. open"]
        day_high = information["2. high"]
        day_close = information["4. close"]
    
        return day_open, day_high, day_close

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0, 0.0, 0.0

def myapp_init():
    day_open, day_high, day_close = my_app()
    day_open = round(float(day_open), 2)
    day_close = round(float(day_close), 2)
    day_high = round(float(day_high), 2)

    output = f"Open: ${day_open}, High: ${day_high}, Close: ${day_close}"
    print('Information for {}: {}'.format(SYMBOL, output))

    
    return output


MY_APP = {
    'name': 'Stock Prices',
    'init': myapp_init
}


if __name__ == '__main__':
    myapp_init()