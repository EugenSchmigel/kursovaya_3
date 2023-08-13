import pytest

from kursovaya_3 import utils
from kursovaya_3.utils import read_data_from_JSON


def test_formated_bill_date():
    assert utils.formated_bill_date('2022-02-22T22:02:22.2022') == '22.02.2022'

def test_formated_bill_to():
    assert utils.formated_bill_to("Счет 96291777776753236930") == "Счет **6930"
    assert utils.formated_bill_to("Visa Platinum 2256483756542539") == "Visa Platinum 2256 48** ****2539"

def test_formated_bill_from():
    assert utils.formated_bill_from("Счет 10848359769870775355") == "Счет **5355"
    assert utils.formated_bill_from("Счет 21969751544412966366") == "Счет **6366"


def test_sorted_by_date():
    assert utils.sorted_by_date([{"date": ""}]) == []
    assert utils.sorted_by_date([{"id": 121646999, "state": "EXECUTED"}]) == []
    assert utils.sorted_by_date([{"date": ""}]) == []
    assert utils.sorted_by_date([{"state": "EXECUTED", "date": "2018-06-08T16:14:59.936274"}]) == []
    assert utils.sorted_by_date([{"date": "2018-06-08T16:14:59.936274", "state": "EXECUTED", "from": "Maestro 7552745726849311"}]) == [{"date": "2018-06-08T16:14:59.936274", "state": "EXECUTED", "from": "Maestro 7552745726849311"}]


def test_sort_data():
    assert utils.sort_data([{"date": "2018-07-08T16:14:59.936274", "date": "2018-08-09T16:14:59.936274"}]) != [{"date": "2018-08-09T16:14:59.936274", "date": "2018-07-08T16:14:59.936274"}]


@pytest.fixture
def test_data():
    return [{'date': '2018-06-08T16:14:59.936274', 'from': 'Maestro 7552745726849311', 'state': 'EXECUTED'}]
def test_read_data_from_JSON(test_data):
    read_data_from_JSON()
    assert test_data == [{"date": "2018-06-08T16:14:59.936274", "state": "EXECUTED", "from": "Maestro 7552745726849311"}]
def test_last_five_operations():
    assert utils.last_five_operations([{"id": 667307132, "state": "EXECUTED", "date": "2019-07-13T18:51:29.313309", "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод с карты на счет", "from": "Maestro 1308795367077170", "to": "Счет 96527012349577388612"}, {"id": 179194306, "state": "EXECUTED", "date": "2019-05-19T12:51:49.023880", "operationAmount": {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "МИР 5211277418228469", "to": "Счет 58518872592028002662"}, {"id": 957763565, "state": "EXECUTED", "date": "2019-01-05T00:52:30.108534", "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 46363668439560358409", "to": "Счет 18889008294666828266"}, {"id": 490100847, "state": "EXECUTED", "date": "2018-12-22T02:02:49.564873", "operationAmount": {"amount": "56516.63", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод с карты на карту", "from": "Visa Gold 8326537236216459", "to": "MasterCard 6783917276771847"}, {"id": 921286598, "state": "EXECUTED", "date": "2018-03-09T23:57:37.537412", "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации", "from": "Счет 26406253703545413262", "to": "Счет 20735820461482021315"}]
) == [{"id": 667307132, "state": "EXECUTED", "date": "2019-07-13T18:51:29.313309", "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод с карты на счет", "from": "Maestro 1308795367077170", "to": "Счет 96527012349577388612"}, {"id": 179194306, "state": "EXECUTED", "date": "2019-05-19T12:51:49.023880", "operationAmount": {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "МИР 5211277418228469", "to": "Счет 58518872592028002662"}, {"id": 957763565, "state": "EXECUTED", "date": "2019-01-05T00:52:30.108534", "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 46363668439560358409", "to": "Счет 18889008294666828266"}, {"id": 490100847, "state": "EXECUTED", "date": "2018-12-22T02:02:49.564873", "operationAmount": {"amount": "56516.63", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод с карты на карту", "from": "Visa Gold 8326537236216459", "to": "MasterCard 6783917276771847"}, {"id": 921286598, "state": "EXECUTED", "date": "2018-03-09T23:57:37.537412", "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации", "from": "Счет 26406253703545413262", "to": "Счет 20735820461482021315"}]


def test_get_last_formated_operation():
    assert utils.get_last_formated_operation([{"id": 667307132, "state": "EXECUTED", "date": "2019-07-13T18:51:29.313309", "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод с карты на счет", "from": "Maestro 1308795367077170", "to": "Счет 96527012349577388612"}]
) != """13.07.2019 Перевод с карты на счет\nMaestro 1308 79** ****7170 -> Счет **8612\n97853.86 руб."""