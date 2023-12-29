import openpyxl
# import os
# from pythonProject import yandexdisk
import yandexdisk


def get_value_from_xlsx():
    # os.chdir("C:\\Users\\uka\\Downloads")
    yandexdisk.get_file_from_yadisk()
    wb = openpyxl.load_workbook('Бюджет.xlsx', data_only=True)
    sheet = wb['Валютные_спекуляции']
    cell = sheet['F86'].value
    return cell
