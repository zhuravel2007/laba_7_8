import json
import os

FILE_NAME = "questions.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def is_valid_question(question):
    if len(question) <= 3:
        return False
    if question.isdigit():
        return False
    return True

def handle_form(mail, username, question):
    if not is_valid_question(question):
        print("Ошибка ввода")
        return

    data = load_data()

    if mail not in data:
        data[mail] = [username, []]

    if question not in data[mail][1]:
        data[mail][1].append(question)

    save_data(data)
    print("Сохранено")

handle_form("user@mail.com", "Ivan", "Как работает pdb?")
handle_form("user@mail.com", "Ivan", "Что такое JSON?")
handle_form("user@mail.com", "Ivan", "Как работает pdb?")
handle_form("new@mail.com", "Anna", "Как открыть файл?")
handle_form("user@mail.com", "Ivan", "hi")
handle_form("user@mail.com", "Ivan", "12345")
handle_form("user@mail.com", "Ivan", "Ошибка 404 что значит?")
handle_form("user@mail.com", "Ivan", "")
handle_form("user@mail.com", "Ivan", "Очень длинный вопрос про Python и отладку")
handle_form("a@mail.com", "A", "Question 1")
handle_form("b@mail.com", "B", "Question 2")
handle_form("c@mail.com", "C", "Question 3")