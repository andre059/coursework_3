import json

from utils import filter_data, last_recent_values, format_data


def mein():
    """
<<<<<<< HEAD
    Получение json данных , завершение программы если нет данных, вывод данных для пользователя
=======
    Получение json данных и завершение программы если нет данных
>>>>>>> 2396fa1 (закончил)
    :return:
    """
    with open('data_file.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)

        if not data:
            exit('Нет данных')
        else:
            print('Информация получена успешно !\n')

        filtered_from = True
<<<<<<< HEAD
        recent_values = 5
=======
        recent_values = 5  # последние значения
>>>>>>> 2396fa1 (закончил)

        data = filter_data(data, filtered_from)
        data = last_recent_values(data, recent_values)
        data = format_data(data)

        print(f'Вывод данных:\n')
<<<<<<< HEAD

        for row in data:

=======
        for row in data:
>>>>>>> 2396fa1 (закончил)
            print(row, end='\n\n')


if __name__ == '__main__':
    mein()
