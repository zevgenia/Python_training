from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    contact = Contact(firstname="Анна", lastname="Иванова", address="ул.Смольная, д.18", homephone="(495)123-12-23",
                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20", secondaryphone="(495)1820",
                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contacts_list() # считываем старый список со страницы
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id #добавляем недостающий id в объект типа контакт
    app.contact.modify_contact_by_index(index, contact) # передаем объект в функцию модификации
    new_contacts = app.contact.get_contacts_list() # считываем новый список со страницы
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact # меняем контакт в старом списке вручную
    print("\nold_contacts", old_contacts)
    print("new_contacts", new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact(app):
    contact = Contact(firstname="Елена", lastname="Краснова")# создаем объект контакт
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contacts_list() # считываем старый список со страницы
    contact.id = old_contacts[0].id #добавляем недостающий id в объект типа контакт
    app.contact.modify_first_contact(contact) # передаем объект в функцию модификации
    new_contacts = app.contact.get_contacts_list() # считываем новый список со страницы
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact # меняем первый контакт в старом списке вручную
    print("\nold_contacts", old_contacts)
    print("new_contacts", new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
