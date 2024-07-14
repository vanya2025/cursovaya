import json
from datetime import datetime

def mask_card_number(card_number):
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"

def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

def get_last_five_operations(file_path):
    with open(file_path, 'r') as file:
        operations = json.load(file)

    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

    last_five_operations = sorted_operations[:5]

    for op in last_five_operations:
        date = format_date(op['date'])
        description = op['description']
        from_account = mask_card_number(op['from']) if 'from' in op else ''
        to_account = mask_account_number(op['to']) if 'to' in op else ''
        amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}"

        print(f"{date} {description}")
        if from_account:
            print(f"{from_account} -> {to_account}")
        else:
            print(f"{to_account}")
        print(f"{amount}\n")
