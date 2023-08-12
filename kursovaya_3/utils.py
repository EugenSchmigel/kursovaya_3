import json

def read_data_from_JSON():
    """load JSON file content"""
    with open('operations.json', encoding='utf-8') as operations_file:
        # assign the loaded content to the variable "data"
        data = json.load(operations_file)
        return data


def sorted_by_date(data):
    """sort and clean the content in "data" """
    # add new variable to store the clean data
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
        # add the clean data to the variable "validate_operation"
        validate_operation.append(operation)
    return validate_operation

def formated_bill_date(bill_date):
    """ formate the date from 'YYYY-MM-DDTHH:MM:SS.ms' to 'DD.MM.YYYY' """
    # split the date string by the sign "T" -> ['YYYY-MM-DD', 'HH:MM:SS.ms']
    bill_date_splitted_by_date = bill_date.split('T')
    # split the first list value by the sign "-" -> ['YYYY', 'MM', 'DD']
    splitted_bill_date = bill_date_splitted_by_date[0].split('-')
    # join the list by the sign '.' and reverse the list values -> DD.MM.YYYY
    bill_date_formated = '.'.join(reversed(splitted_bill_date))
    return bill_date_formated


def formated_bill_to(bill_to):
    """ formate the bill to number and card info  """
    # split the card info
    card_info_to = bill_to.split()
    # last value (number) from the card info
    number = card_info_to[-1]
    # if the bill_to string starts with 'счет'
    if bill_to.lower().startswith('счет'):
        # then format the card info as following
        # mask all numbers expect the last four
        musked_number = f"{card_info_to[0]} **{number[-4:]}"
        return musked_number

    # otherwise do following
    else:
        # mask from the first to fourth digit then one space sign ... last four digits visible
        musked_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
        # add the above value 'masked_number' to the list 'card_info_to'
        card_info_to[-1] = musked_number

    # join the 'card_info_to' to a string
    hidden_bill_info_to = ' '.join(card_info_to)

    return hidden_bill_info_to


def formated_bill_from(bill_from):
    """ formate the bill to number and card info"""
    # split the card info
    card_info_from = bill_from.split()
    # last value (number) from the card info
    number = card_info_from[-1]
    # if the bill_from string starts with 'счет'
    if bill_from.lower().startswith('счет'):
        # then format the card info as following
        # mask all numbers expect the last four
        musked_number = f"{card_info_from[0]} **{number[-4:]}"
        return musked_number
    else:
        # mask from the first to fourth digit then one space sign ... last four digits visible
        musked_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
        # add the above value 'masked_number' to the list 'card_info_from'
        card_info_from[-1] = musked_number

    # join the 'card_info_from' to a string
    hidden_bill_info_from = ' '.join(card_info_from)

    return hidden_bill_info_from


def sort_data(validated_operation):
    """ sort the validated data """
    # add the list 'validated_operation' to the function 'sorted' and sort by "operation['date']"
    # and reverse (latest data on top) the data
    sorted_data = sorted(validated_operation, key=lambda operation: operation['date'], reverse=True)
    return sorted_data


def last_five_operations(validated_operation):
    """ display last five operations"""
    # count of the operations. 5 operations visible by default.
    # If you need more the 5 operations then adjust the below variable 'operation_count'
    operation_count = 5
    last_five_operartions = sort_data(validated_operation[-operation_count-1:-1])
    return last_five_operartions


def get_last_formated_operation(last_five_operartions):
    """ Display formatted five operation  """
    # read values from the operations and store it in variables
    for operation in last_five_operartions:
        bill_date = operation['date']
        bill_description = operation['description']
        bill_from = operation['from']
        bill_to = operation['to']

        bill_amount = operation['operationAmount']['amount']
        bill_currency = operation['operationAmount']['currency']['name']

        # call the format function and save the value to a variable
        bill_date_formated = formated_bill_date(bill_date)
        bill_to_formated = formated_bill_to(bill_to)
        bill_from_formated = formated_bill_from(bill_from)

        # display the formatted operation informations
        print(f"""
    {bill_date_formated} {bill_description}
    {bill_from_formated} -> {bill_to_formated}
    {bill_amount} {bill_currency}""")


