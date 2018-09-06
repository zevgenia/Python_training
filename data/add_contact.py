from model.contact import Contact
import random
import string

constant = [

    Contact(firstname="Анна", lastname="Иванова", address="ул.Смольная, д.18", homephone="(495)123-12-23",
            mobilephone="903-456-12-12", workphone="+7(495)120 18 20", secondaryphone="(495)1820",
            email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт

]


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
    for i in range(5)
]
