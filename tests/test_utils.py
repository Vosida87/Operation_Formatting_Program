from utils import get_data, get_operations, date_sort, changing_the_date_display
from utils import changing_the_account_number_display, get_last_five_operations

# Импортировал функции с utils для их тестирования

def test_get_data():
    """
    для теста создал файл test_operations.json с небольшим количеством данных
    """
    assert get_data('test_operations.json') == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
      "amount": "50870.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 4598300720424501",
    "to": "Счет 43597928997568165086"
  }
]
data = get_data('test_operations.json')

def test_get_operations():
    assert len(get_operations(data)) == 2

data = get_operations(data)

def test_date_sort():

  # expect - то, что мы ожидаем, а список result собирает данные, которые вернёт функция

  expect = ["2018-01-26T15:40:13.413061", "2019-08-26T10:50:58.294041"]
  result = []
  data_test = date_sort(data)
  for date in data_test:
    result.append(date['date'])
  assert result == expect

def test_changing_the_date_display():
  expect = ['26.08.2019', '26.01.2018']
  result = []
  data_test = changing_the_date_display(data)
  for date in data_test:
    result.append(date['date'])
  assert result == expect

def test_changing_the_account_number_display():
  expect = ['Maestro 5968 37** **** 5199', 'Maestro 5983 00** **** 4501']
  result = []
  data_test = changing_the_account_number_display(data)
  for number in data_test:
    result.append(number['from'])

  # new_data - новые данные для обработки, чтобы проверить сценарии в функции

  new_data = [
    {
      "id": 596171168,
      "state": "EXECUTED",
      "date": "2018-07-11T02:26:18.671407",
      "operationAmount": {
        "amount": "79931.03",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Открытие вклада",
      "to": "Счет 72082042523231456215"
    },
    {
      "id": 522357576,
      "state": "EXECUTED",
      "date": "2019-07-12T20:41:47.882230",
      "operationAmount": {
        "amount": "51463.70",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Счет 48894435694657014368",
      "to": "Счет 38976430693692818358"
    },
    {
      "id": 536723678,
      "state": "EXECUTED",
      "date": "2018-06-12T07:17:01.311610",
      "operationAmount": {
        "amount": "26334.08",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Visa Classic 4195191172583802",
      "to": "Счет 17066032701791012883"
    },
  ]
  new_data = changing_the_account_number_display(new_data)
  new_expect = ['**6215', '**8358', '**2883']
  new_result = []
  for number in new_data:
    new_result.append(number["to"])
  assert result == expect
  assert new_result == new_expect

def test_get_last_five_operations():
  expect = ['26.08.2019', '26.01.2018']
  result = []
  data_test = get_last_five_operations(data)
  for date in data_test:
    result.append(date['date'])
  assert result == expect
