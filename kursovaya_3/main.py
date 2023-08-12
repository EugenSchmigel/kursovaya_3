from utils import read_data_from_JSON
from utils import sorted_by_date
from utils import last_five_operations
from utils import get_last_formated_operation


data = read_data_from_JSON()

validated_operation = sorted_by_date(data)

last_five_operartions = last_five_operations(validated_operation)

get_last_formated_operation(last_five_operartions)