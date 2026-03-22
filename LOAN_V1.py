from datetime import datetime
from openpyxl import load_workbook

RENTALS_FILE = "C:/Users/markb/OneDrive/Documents/APSC 103/iCons Folders/iCon Equipment Rentals 2024-26.xlsx"

def process_loan(data: dict):
    """
    Main function called by GUI
    """

    record = build_record(data)
    write_to_excel(record)


def build_record(data):
    """
    Applies business logic rules
    """

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %I:%M %p")

    return {
        "Date": formatted_time,
        "First Name": data["first_name"],
        "Last Name": data["last_name"],
        "Equipment": data["equipment"],
        "Amount": data["amount"],
        "Student Card Taken": data["student_card_taken"],
        "Signed Out": data["student_card_taken"],  # automatic
        "Signed In": False,  # always false on loan
        "Comments": ""
    }


def write_to_excel(record):
    """
    Appends a new row to Excel
    """

    try:
        wb = load_workbook(RENTALS_FILE)
        ws = wb.active  # assumes first sheet is correct

        new_row = [
            record["Date"],
            record["First Name"],
            record["Last Name"],
            record["Equipment"],
            record["Amount"],
            record["Student Card Taken"],
            record["Signed Out"],
            record["Signed In"],
            record["Comments"]
        ]

        ws.append(new_row)

        wb.save(RENTALS_FILE)

        print("✅ Loan successfully written to Excel")

    except Exception as e:
        print(f"❌ Error writing to Excel: {e}")
