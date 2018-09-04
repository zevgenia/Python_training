# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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


@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    print("\nold_contacts", old_contacts)
    print("new_contacts", new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# testdata1 = [
#    Contact(firstname="Иван", lastname="Смирнов", address="ул.Бабушкина, д.18", homephone="(495)123-12-23",
#                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20", secondaryphone="(495)1820",
#                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org"),# создаем объект контакт,
#    Contact(firstname="Валентина", lastname="Петрова", address="шоссе Энтузиастов, д.18", mobilephone="(901)123-12-23",
#                      email="qwerty@gmail.com")
# ]

