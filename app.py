import pdb

questions = {}

def handle_form(mail, username, question):
    questions[mail] = [username, question]
    pdb.set_trace()

handle_form("user@mail.com", "Ivan", "Как работает pdb?")