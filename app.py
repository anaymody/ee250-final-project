import requests
import json

def my_app():
    url = 'https://api.adviceslip.com/advice'
    r = requests.get(url)

    if r.status_code == 200: # Status: OK
        data = r.json()
        
        print(data['slip']['advice'])
        return data['slip']['advice']

    else:
        print("Error!")
        

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