import json

from utils import filter_data, last_recent_values, format_data


def mein():
    """
    Получение json данных и завершение программы если нет данных
    :return:
    """
    with open('data_file.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)

        if not data:
            exit('Нет данных')
        else:
            print('Информация получена успешно !\n')

        filtered_from = True
        recent_values = 5  # последние значения

        data = filter_data(data, filtered_from)
        data = last_recent_values(data, recent_values)
        data = format_data(data)

        print(f'Вывод данных:\n')
        for row in data:
            print(row, end='\n\n')


if __name__ == '__main__':
    mein()
