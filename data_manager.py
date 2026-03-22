import pandas as pd
from datetime import datetime

INVENTORY_FILE = "inventory.xlsx"
TRANSACTION_FILE = "transactions.xlsx"


def update_stock(equipment_name, quantity_change):
    df = pd.read_excel(INVENTORY_FILE)

    if equipment_name in df["Equipment"].values:
        df.loc[df["Equipment"] == equipment_name, "Stock"] += quantity_change
        df.to_excel(INVENTORY_FILE, index=False)
    else:
        print("Equipment not found")


def add_transaction(student_id, name, equipment, qty, trans_type):
    df = pd.read_excel(TRANSACTION_FILE)

    new_row = {
        "Student ID": student_id,
        "Name": name,
        "Equipment": equipment,
        "Qty": qty,
        "Type": trans_type,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(TRANSACTION_FILE, index=False)


def search_user_transactions(student_id):
    df = pd.read_excel(TRANSACTION_FILE)
    return df[df["Student ID"] == student_id]
