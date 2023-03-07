import requests
def crb_valute() -> None:
    """
    Функция выводит курс валют
    с сайта ЦРБ за вчера и сегодня.
    """
    valute_name = str(input())
    valute_name = valute_name.upper()
    local_serv = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    val_dict = dict(local_serv.json())
    if valute_name in val_dict['Valute']:
        print("Вчера один", (val_dict['Valute'][valute_name]['Name']), "был равен",
              (val_dict['Valute'][valute_name]['Value']), "руб.")
        print("Сегодня один", (val_dict['Valute'][valute_name]['Name']), "равен",
              (val_dict['Valute'][valute_name]['Previous']), "руб.")
    else:
        print("Указанная валюта не найдена")
crb_valute()