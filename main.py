import json
from datetime import datetime
from utils import mask_card_number, mask_account_number, format_date

def get_last_five_operations(file_path):
    with open(file_path, 'r') as file:
        operations = json.load(file)

    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

    last_five_operations = sorted_operations[:5]

    result = []
    for op in last_five_operations:
        date = format_date(op['date'])
        description = op['description']
        from_account = mask_card_number(op['from']) if 'from' in op else ''
        to_account = mask_account_number(op['to']) if 'to' in op else ''
        amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}"

        operation_info = f"{date} {description}\n"
        if from_account:
            operation_info += f"{from_account} -> {to_account}\n"
        else:
            operation_info += f"{to_account}\n"
        operation_info += f"{amount}\n"
        result.append(operation_info)

    return result

if __name__ == "__main__":
    operations = get_last_five_operations('operations.json')
    for operation in operations:
        print(operation)