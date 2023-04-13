from utils import get_data, get_operations, date_sort, get_last_five_operations
from utils import changing_the_date_display, changing_the_account_number_display

# Импортурем функции для основной программы

def main():

    # Собираем и сортируем данные функциями из data_utils

    data = get_data('operations.json')
    executed_data = get_operations(data)
    sorted_data = date_sort(executed_data)
    required_data = get_last_five_operations(sorted_data)

    # Изменяем отображение некоторых данных для пользователя

    new_date_data = changing_the_date_display(required_data)
    new_number_data = changing_the_account_number_display(new_date_data)

    # Изменяем порядок вывода операций, чтобы сначала отображались последние

    new_number_data.reverse()

    # Перебор операций с отображением нужных данных пользователю

    print(' ')
    for operation in new_number_data:
        if 'Открытие вклада' == operation["description"]:
            print(
                f"{operation['date']} {operation['description']}\n"
                f"{operation['to']}\n"
                f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
            )
            print(' ')
        else:
            print(
                f"{operation['date']} {operation['description']}\n"
                f"{operation['from']} -> {operation['to']}\n"
                f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
            )
            print(' ')

if __name__ == '__main__':
    main()
