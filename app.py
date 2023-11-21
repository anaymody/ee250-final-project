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
        

# def myapp_init():
#     advice = myapp()

#     output = f"Open: ${day_open}, High: ${day_high}, Close: ${day_close}"
#     print('Information for {}: {}'.format(SYMBOL, output))

    
#     return output


MY_APP = {
    'name': 'Stock Prices',
    'init': myapp
}


if __name__ == '__main__':
    myapp()