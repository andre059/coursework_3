from  datetime import datetime


def filter_data(data, filtered_from=False):
    """
    Филтьтрация данных, проведена операция или отменена, известен ли счет от которого был сделан перевод
    :param filtered_from:
    :param data:
    :return:
    """
    data = [item for item in data if 'state' in item and item['state'] == 'EXECUTED']

    if filtered_from:
        data = [item for item in data if 'from' in item]

    return data


def last_recent_values(data, recent_values):
    """
    Сортировка данных по ключу 'date'
    :param data:
    :param recent_values:
    :return:
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:recent_values]

    return data


def format_data(data):
    """
    Преобразоавние информации в читабельные данные для пользователя
    :param data:
    :return:
    """
    formatted = []

    for row in data:
        data = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']

        sender_info, sender_bill = '', ''

        if 'from' in row:
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}'
            sender_info = ''.join(sender)

        to = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted.append(f"""\
{data} {description} 
{sender_info} {sender_bill} -> {to} 
{operation_amount}""")

    return formatted
