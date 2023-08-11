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
        validate_operation.append(operation)

        if 'date' in operation and operation['date']:
            validate_operation.append(operation)
    return validate_operation

validated_operation = sorted_by_date(data)

def sort_data(validated_operation):
    sorted_data = sorted(validated_operation, key=lambda operation: operation['date'], reverse=True)
    return pprint(sorted_data)

sort_data(validated_operation[-3:-1])

