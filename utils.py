from datetime import datetime

def mask_card_number(card_number):
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"

def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")