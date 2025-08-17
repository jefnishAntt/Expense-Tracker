import csv
from datetime import datetime

FILE_PATH = 'expenses.csv'

def save_expenses(expenses):
    with open(FILE_PATH, mode='a', newline='', encoding='utf-8') as file:

        field_names = ["Category", "Amount", "Date"]
        writer = csv.DictWriter(file, fieldnames=field_names)

        if not file:
            writer.writeheader()
        
        for expense in expenses:
            writer.writerow( expense )
            

def add_expense():
    expenses = []
    category = input("Category: ").strip()
    amount = float(input("Amount: ").strip())
    date_input = input("Date (DD-MM-YYYY) [default: today]:").strip()
    
    if date_input:
        date = datetime.strptime(date_input, '%d-%m-%Y').strftime("%d-%m-%Y")
    else:
        date = datetime.today().strftime("%d-%m-%Y")

    expense_format = {"Category": category, "Amount": amount, "Date": date}
    expenses.append(expense_format)

    save_expenses(expenses)
    print("✅ Expense Added Successfully!")

def clear_expense():
    with open(FILE_PATH, mode='w', encoding='utf-8') as file:
        field_names = ["Category", "Amount", "Date"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

def remove_expense():
    category_to_remove = input("Category name to remove:")
    date_input = ''

    def inner_fuction():
        date_input = input("Date of Category (DD-MM-YYYY):")
        if date_input == 'exit':
            return
        elif date_input:
            date = datetime.strptime(date_input, '%d-%m-%Y')
            with open(FILE_PATH, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                expenses = [expense for expense in reader if (expense['Category'].lower() !=category_to_remove.lower() and expense['Date'] != date)]
            clear_expense()
            save_expenses(expenses)
            print("✅ Expense Removed Successfully!")
        else:
            print('please! provide the date to remove the item or type exit to cancel')
            inner_fuction()
    inner_fuction()