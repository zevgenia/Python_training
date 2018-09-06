# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import testdata as testdata


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

