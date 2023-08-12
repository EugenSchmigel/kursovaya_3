import json

def read_data_from_JSON():
    with open('operations.json', encoding='utf-8') as operations_file:
        data = json.load(operations_file)
        return data


def sorted_by_date(data):
    validate_operation = []
    for operation in data:
        if not operation:
            continue
        elif not 'date' in operation:
            continue
        elif not operation.get('date'):
            continue
        elif not operation.get('from'):
            continue
        elif operation['state'] != 'EXECUTED':
            continue
        validate_operation.append(operation)

        if 'date' in operation and operation['date']:
            validate_operation.append(operation)
    return validate_operation

def formated_bill_date(bill_date):
    bill_date_splitted_by_date = bill_date.split('T')
    splitted_bill_date = bill_date_splitted_by_date[0].split('-')
    bill_date_formated = '.'.join(reversed(splitted_bill_date))
    return bill_date_formated


def formated_bill_to(bill_to):
    card_info_to = bill_to.split()
    number = card_info_to[-1]
    if bill_to.lower().startswith('счет'):
        musked_number = f"{card_info_to[0]} **{number[-4:]}"
        return musked_number

    else:
        musked_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
        card_info_to[-1] = musked_number
    hidden_bill_info_to = ' '.join(card_info_to)
    return hidden_bill_info_to


def formated_bill_from(bill_from):
    card_info_from = bill_from.split()
    number = card_info_from[-1]
    if bill_from.lower().startswith('счет'):
        musked_number = f"{card_info_from[0]} **{number[-4:]}"
        return musked_number
    else:
        musked_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
        card_info_from[-1] = musked_number
    hidden_bill_info_from = ' '.join(card_info_from)
    return hidden_bill_info_from


def sort_data(validated_operation):
    sorted_data = sorted(validated_operation, key=lambda operation: operation['date'], reverse=True)
    return sorted_data


def last_five_operations(validated_operation):
    operation_count = 5
    last_five_operartions = sort_data(validated_operation[-operation_count-1:-1])
    return last_five_operartions


def get_last_formated_operation(last_five_operartions):
    for operation in last_five_operartions:
        bill_date = operation['date']
        bill_description = operation['description']
        bill_from = operation['from']
        bill_to = operation['to']

        bill_amount = operation['operationAmount']['amount']
        bill_currency = operation['operationAmount']['currency']['name']

        bill_date_formated = formated_bill_date(bill_date)
        bill_to_formated = formated_bill_to(bill_to)
        bill_from_formated = formated_bill_from(bill_from)

        print(f"""
    {bill_date_formated} {bill_description}
    {bill_from_formated} -> {bill_to_formated}
    {bill_amount} {bill_currency}""")


