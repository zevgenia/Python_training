from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string_firstname(maxlen):  #генератор случайных строк для имени
    simbols = ["Елена", "Сергей", "Дмитрий", "Алексей", "Алла", "Мария"]
    return random.choice(simbols)


def random_string_lastname(maxlen):  #генератор случайных строк для фамилии
    simbols = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ" + " "
    return "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


def random_string_address(prefix, maxlen):  #генератор случайных строк для адреса
    simbols = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ" + string.digits + " "*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


def random_string_phone(prefix, maxlen):  #генератор случайных строк для номера телефона
    simbols = string.digits + "() -"*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


def random_string_email( maxlen):  #генератор случайных строк для email
    domains = ["hotmail.com", "gmail.com", "aol.org", "mail.com", "yandex.ru", "yahoo.com"]
    simbols = string.ascii_letters + string.digits
    return ("".join([random.choice(simbols) for i in range(random.randrange(maxlen))]) +"@"+ random.choice(domains))


# тестовые данные генерируются с помощью генератора случайных строк
testdata = [
    Contact(firstname=random_string_firstname(10), lastname=random_string_lastname(15),
            address=random_string_address("адрес:", 30),
            mobilephone=random_string_phone("+", 14), email=random_string_email(20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

