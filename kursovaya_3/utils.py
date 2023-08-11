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

last_five_operartions = sort_data(validated_operation[-25:-1])

def formated_bill_date(bill_date):
    bill_date_splitted_by_date = bill_date.split('T')
    splitted_bill_date = bill_date_splitted_by_date[0].split('-')
    bill_date_formated = '.'.join(reversed(splitted_bill_date))
    return bill_date_formated

def formated_bill_to(bill_to):
    pass
def formated_bill_from(bill_from):
    card_info = bill_to.split()
    number = card_info[-1]
    if bill_to.lower().startswith("Счет"):
        musked_number = f"**{number[-4:]}"
        return musked_number
    else:
        musked_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
        card_info[-1] = musked_number
    hidden_bill_info = ' '.join(card_info)
    return hidden_bill_info


for operation in last_five_operartions:
    bill_date = operation['date']
    bill_description = operation['description']
    bill_from = operation['from']
    bill_to = operation['to']
    bill_amount = operation['operationAmount']['amount']
    bill_currency = operation['operationAmount']['currency']['name']

    print(f"""{formated_bill_date(bill_date)} {bill_description}
    {formated_bill_from(bill_from)} -> {bill_to}
{bill_amount} {bill_currency}""")

