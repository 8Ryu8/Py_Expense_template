from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions, init_expense_report, new_expense
from user import user_questions, add_user

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.2",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_options']) == "New User":
        add_user()
        ask_option()

def main():
    # init the 'expense_report.csv' file with column names
    init_expense_report()
    ask_option()

main()