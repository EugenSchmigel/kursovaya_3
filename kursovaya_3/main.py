from utils import read_data_from_JSON
from utils import sorted_by_date
from utils import formated_bill_date
from utils import formated_bill_to
from utils import formated_bill_from
from utils import last_five_operations


data = read_data_from_JSON()

validated_operation = sorted_by_date(data)

last_five_operartions = last_five_operations(validated_operation)

for operation in last_five_operartions:
    bill_date = operation['date']
    bill_description = operation['description']
    bill_from = operation['from']
    bill_to = operation['to']
    bill_amount = operation['operationAmount']['amount']
    bill_currency = operation['operationAmount']['currency']['name']

    print(bill_date, bill_description)
#     print(f"""
# {formated_bill_date(bill_date)} {bill_description}
# {formated_bill_from(bill_from)} -> {formated_bill_to(bill_to)}
# {bill_amount} {bill_currency}""")