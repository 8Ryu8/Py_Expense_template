from PyInquirer import prompt
import csv

# Find all users
def get_users_options(answers=""):
    f = open('users.csv', 'r')
    # read all lines without ending '\n'
    users = [line[:-1] for line in f]
    print("users: ", users)
    return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":'list',
        "name":"spender",
        "message":"New Expense - Spender: ",
        'choices': get_users_options,
    },
    {
        # Can choose involved people among the list of users
        # spender is not automatically selected soz
        "type":"checkbox",
        "name":"involved people",
        "message":"NewExpense - Involved people:",
        'choices': [{'name': n } for n in get_users_options()],
    }

]

# Init columns names in the .csv file
def init_expense_report():
    f = open('expense_report.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(["amount", "label", "spender"])
    f.close()

# Add a new line in .csv file for a new expense
def fill_expense_report(infos):
    f = open('expense_report.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(infos)
    f.close()

def new_expense(*args):
    infos = prompt(expense_questions)
    fill_expense_report(infos.values())
    print("Expense Added !")
    return True


