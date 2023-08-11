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


for operation in last_five_operartions:
    bill_date = operation['date']
    bill_description = operation['description']
    bill_from = operation['from']
    bill_to = operation['to']
    bill_amount = operation['operationAmount']['amount']
    bill_currency = operation['operationAmount']['currency']['name']

    bill_date_splitted_by_date = bill_date.split('T')
    splitted_bill_date = bill_date_splitted_by_date[0].split('-')
    bill_date_formated = '.'.join(reversed(splitted_bill_date))

    print(f"""{bill_date_formated} {bill_description}
    {bill_from} {bill_to}
{bill_amount} {bill_currency}""")

