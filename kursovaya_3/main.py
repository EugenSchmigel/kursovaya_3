from utils import read_data_from_JSON
from utils import sorted_by_date
from utils import last_five_operations
from utils import get_last_formated_operation

# load JSON file content
data = read_data_from_JSON()

#"sort and clean the content in "data"
validated_operation = sorted_by_date(data)

# last five operations
last_five_operartions = last_five_operations(validated_operation)

# display formatted five operation
get_last_formated_operation(last_five_operartions)