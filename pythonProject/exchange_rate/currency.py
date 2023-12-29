import json

import requests

def get_currency(valute):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    dict_currency = json.loads(response.text)
    if valute in dict_currency['Valute']:
        return dict_currency['Valute'][valute]['CharCode'], dict_currency['Valute'][valute]['Nominal'], dict_currency['Valute'][valute]['Value']
    return 0, 0, 0