import json

import requests


def get_currency(valute):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    dict_currency = json.loads(response.text)
    return dict_currency['Valute'][valute]['CharCode'], dict_currency['Valute'][valute]['Nominal'], dict_currency['Valute'][valute]['Value']

def get_valute():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    dict_currency = json.loads(response.text)
    list_currency = []
    for key in dict_currency['Valute'].keys():
        list_currency.append(key)
        currency = ', '.join(list_currency)
    return currency

#print(get_valute())
#valute = input('Введите код валюты:')
#valute_from_response, nom, course = get_currency(valute)
#print(f'Курс: {nom} {valute_from_response} стоит {course} RUB')
