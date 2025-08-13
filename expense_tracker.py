import csv
from datetime import datetime

FILE_PATH = 'expenses.csv'

def save_expenses(category, amount, date):
    expenses =[]
    with open(FILE_PATH, mode='a', newline='', encoding='utf-8') as file:

        field_names = ["Category", "Amount", "Date"]
        writer = csv.DictWriter(file, fieldnames=field_names)

        if not file:
            writer.writeheader()
        
        writer.writerow({
            "Date": date,
            "Category": category,
            "Amount": amount
        })
            
            


def add_expense():
    category = input("Category: ").strip()
    amount = float(input("Amount: ").strip())
    date_input = input("Date (DD-MM-YYYY) [default: today]:").strip()
    
    if date_input:
        date = datetime.strptime(date_input, '%d-%m-%Y')
    else:
        date = datetime.today()
    
    save_expenses(category, amount, date)
    print("✅ Expense Added Successfully!")

add_expense()