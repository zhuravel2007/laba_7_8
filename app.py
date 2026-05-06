import pdb

questions = {}

def handle_form(mail, question):
    questions[mail] = question
    pdb.set_trace()

handle_form("user@mail.com", "Как работает pdb?")