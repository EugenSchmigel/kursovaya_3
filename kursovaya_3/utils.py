import json
from pprint import pprint


with open('operations.json', encoding='utf-8') as operations_file:

    data = json.load(operations_file)

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

validated_operation = sorted_by_date(data)

def sort_data(validated_operation):
    sorted_data = sorted(validated_operation, key=lambda operation: operation['date'], reverse=True)
    return sorted_data

operation_count = 5
last_five_operartions = sort_data(validated_operation[-operation_count-1:-1])

def formated_bill_date(bill_date):
    bill_date_splitted_by_date = bill_date.split('T')
    splitted_bill_date = bill_date_splitted_by_date[0].split('-')
    bill_date_formated = '.'.join(reversed(splitted_bill_date))
    return bill_date_formated

def formated_bill_to(bill_to):
    card_info_to = bill_to.split()
    number = card_info_to[-1]
    if bill_to.lower().startswith("Счет"):
        musked_number = f"**{number[-4:]}"
        return musked_number

    else:
        musked_number = f"**{number[-4:]}"
        card_info_to[-1] = musked_number
    hidden_bill_info_to = ' '.join(card_info_to)
    return hidden_bill_info_to

#Счет **9638
def formated_bill_from(bill_from):
    card_info_from = bill_to.split()
    number = card_info_from[-1]
    if bill_to.lower().startswith("Счет"):
        musked_number = f"**{number[-4:]}"
        return musked_number
    else:
        musked_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
        card_info_from[-1] = musked_number
    hidden_bill_info_from = ' '.join(card_info_from)
    return hidden_bill_info_from


for operation in last_five_operartions:
    bill_date = operation['date']
    bill_description = operation['description']
    bill_from = operation['from']
    bill_to = operation['to']
    bill_amount = operation['operationAmount']['amount']
    bill_currency = operation['operationAmount']['currency']['name']

    print(f"""
{formated_bill_date(bill_date)} {bill_description}
{formated_bill_from(bill_from)} -> {formated_bill_to(bill_to)}
{bill_amount} {bill_currency}""")


