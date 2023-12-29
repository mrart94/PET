import PySimpleGUI as sg
import currency
import req
import excel

sg.theme('LightGray1')
# Устанавливаем цвет внутри окна
layout = [
          [sg.Text('Доступные валюты: ' + req.get_valute(), size=(60, 4))],
          [sg.Text(f'Доступно: {excel.get_value_from_xlsx()} USD', size=(22, 1))],
          [sg.Text('Введите количество валюты:', size=(22, 1)), sg.InputText(size=(17, 22))],
          [sg.Text('Выберите валюту:', size=(22, 1)), sg.Combo((req.get_valute()).split(', '), default_value='AUD',
           size=(15, 22), enable_events=True, readonly=True)],
          [sg.Button('Ввод'), sg.Button('Отмена')],
          [sg.Text('Итого:', size=(22, 1))],
          [sg.Output(size=(70, 1), key='OUT')]
         ]

# Создаем окно
window = sg.Window('Считаем мою копилку', layout)

# Цикл для обработки "событий" и получения "значений" входных данных
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Отмена':
        # если пользователь закрыл окно или нажал «Отмена»
        break

    count = values[0]
    valute = values[1]
    if count == '':
        count = excel.get_value_from_xlsx()
    else:
        count = int(count)
    valute_from_response, nom, course = currency.get_currency(valute.upper())
    window['OUT'].update(f'Итого: {round((course * count), 2)} руб.')
window.close()
