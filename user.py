from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

# Add a new line in .csv file for a new user
def fill_user_file(infos):
    f = open('users.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(infos)
    f.close()

def add_user():
    infos = prompt(user_questions)
    fill_user_file(infos.values())
    print("User Added !")
    return True