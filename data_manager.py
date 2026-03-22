import pandas as pd
from datetime import datetime

INVENTORY_FILE = "inventory.xlsx"
TRANSACTIONS_FILE = "transactions.xlsx"


# ==============================
# INVENTORY FUNCTIONS
# ==============================

def load_inventory():
    try:
        return pd.read_excel(INVENTORY_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Equipment", "Stock"])
        df.to_excel(INVENTORY_FILE, index=False)
        return df


def save_inventory(df):
    df.to_excel(INVENTORY_FILE, index=False)


def update_stock(equipment_name, change):
    df = load_inventory()

    if equipment_name in df["Equipment"].values:
        df.loc[df["Equipment"] == equipment_name, "Stock"] += change
    else:
        new_row = pd.DataFrame([[equipment_name, max(0, change)]],
                               columns=["Equipment", "Stock"])
        df = pd.concat([df, new_row], ignore_index=True)

    df["Stock"] = df["Stock"].clip(lower=0)
    save_inventory(df)


def get_stock(equipment_name):
    df = load_inventory()
    row = df[df["Equipment"] == equipment_name]
    if not row.empty:
        return int(row.iloc[0]["Stock"])
    return 0


# ==============================
# TRANSACTION FUNCTIONS
# ==============================

def load_transactions():
    try:
        return pd.read_excel(TRANSACTIONS_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "StudentID", "FirstName", "LastName",
            "Equipment", "Quantity", "Type", "DateTime"
        ])
        df.to_excel(TRANSACTIONS_FILE, index=False)
        return df


def save_transactions(df):
    df.to_excel(TRANSACTIONS_FILE, index=False)


def record_transaction(student_id, first_name, last_name,
                       equipment, quantity, trans_type):

    df = load_transactions()

    new_row = pd.DataFrame([[
        student_id,
        first_name,
        last_name,
        equipment,
        quantity,
        trans_type,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]], columns=df.columns)

    df = pd.concat([df, new_row], ignore_index=True)
    save_transactions(df)

    if trans_type == "Loan":
        update_stock(equipment, -quantity)
    elif trans_type == "Return":
        update_stock(equipment, quantity)


# ==============================
# SEARCH / ANALYSIS FUNCTIONS
# ==============================

def get_student_history(student_id):
    df = load_transactions()
    return df[df["StudentID"] == student_id]


def get_equipment_history(equipment_name):
    df = load_transactions()
    return df[df["Equipment"] == equipment_name]


def get_most_popular_equipment():
    df = load_transactions()
    loans = df[df["Type"] == "Loan"]
    return loans["Equipment"].value_counts()


def get_active_loans():
    df = load_transactions()
    loans = df[df["Type"] == "Loan"]
    returns = df[df["Type"] == "Return"]

    loan_counts = loans.groupby("Equipment")["Quantity"].sum()
    return_counts = returns.groupby("Equipment")["Quantity"].sum()

    active = loan_counts.subtract(return_counts, fill_value=0)
    return active[active > 0]]
