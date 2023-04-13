import json
from datetime import datetime

# Импортируем json для работы с данными в нужном файле
# Импортируем datetime для изменения отображения даты

def get_data(path):

    # Функция считывает данные с переданного файлаclea

    with open(path, encoding='utf8') as file:
        data = json.load(file)
    return data

def get_operations(data):

    # Функция собирает данные только выполненых операций

    new_data = [operation for operation in data if 'state' in operation and operation['state'] == 'EXECUTED']
    return new_data

def date_sort(data):

    # Функция сортирует все операции по датам

    new_data = []
    for i in data:
        if i not in new_data:
            new_data.append(i)
    new_data.sort(key=lambda x: x["date"])
    return new_data

def get_last_five_operations(data):

    # Функция считывает пять последних операций клиента

    new_date = data[-5:]
    return new_date

def changing_the_date_display(data):

    # Функция изменяет отображение даты пользователю

    new_date_data = []
    for operation in data:
        new_date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        operation['date'] = new_date
        new_date_data.append(operation)
    return new_date_data

def changing_the_account_number_display(data):

    # Функция изменяет отображение счетов и номеров карт

    new_numbers_data = []
    for operation in data:
        description = operation["description"]

        # Сценарий при открытии вклада

        if 'Открытие вклада' == description:
            operation['to'] = f'**{operation["to"][-4:]}'
            new_numbers_data.append(operation)

        # Сценарии при использовании счёта, Maestro или Visa Classic

        else:
            if 'Счет' in operation['from']:
                operation['to'] = f'**{operation["to"][-4:]}'
                operation['from'] = f'Счет **{operation["from"][-4:]}'
                new_numbers_data.append(operation)
            elif 'Maestro' in operation['from']:
                operation['to'] = f'**{operation["to"][-4:]}'
                operation['from'] = f'Maestro {operation["from"][9:13]} {operation["from"][13:15]}** **** {operation["from"][-4:]}'
                new_numbers_data.append(operation)
            elif 'Visa Classic' in operation['from']:
                operation['to'] = f'**{operation["to"][-4:]}'
                operation['from'] = f'Visa Classic {operation["from"][14:18]} {operation["from"][18:20]}** **** {operation["from"][-4:]}'
                new_numbers_data.append(operation)
    return new_numbers_data
