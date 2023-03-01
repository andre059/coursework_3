from utils import filter_data, last_recent_values, format_data


def test_filter_data(test_data):
    assert len(filter_data(test_data)) == 4
    assert len(filter_data(test_data, filtered_from=True)) == 3


def test_last_recent_values(test_data):
    data = last_recent_values(test_data, 4)
    assert data[1]['date'] == '2019-07-03T18:35:29.512364'
    assert len(data) == 4


def test_format_data(test_data):
    data = format_data(test_data)
    assert data == ['26.08.2019 Перевод организации \nMaestro 1596 83** **** 5199 -> Счет **9589 \n31957.58 руб.', '03.07.2019 Перевод организации \nMasterCard 7158 30** **** 6758 -> Счет **5560 \n8221.37 USD', '30.06.2018 Перевод организации \nСчет 7510 68** **** 6952 -> Счет **6702 \n9824.07 USD', '23.03.2018 Открытие вклада \n  -> Счет **2431 \n48223.05 руб.', '04.04.2019 Перевод со счета на счет \nСчет 1970 86** **** 8542 -> Счет **4188 \n79114.93 USD']



