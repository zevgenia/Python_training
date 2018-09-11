from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui): #проверки из БД
    contact = Contact(firstname="Анна", lastname="Иванова", address="ул.Смольная, д.18", homephone="(495)123-12-23",
                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20", secondaryphone="(495)1820",
                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list() # считываем старый список со страницы
    old_contact = random.choice(old_contacts)
    contact.id = old_contact.id #добавляем недостающий id в новый контакт
    print(contact.id)
    app.contact.modify_contact_by_id(old_contact.id, contact) # передаем объект в функцию модификации
    new_contacts = db.get_contact_list() # считываем новый список со страницы
    assert len(old_contacts) == len(db.get_contact_list())
    # меняем контакт в старом списке вручную
    old_contacts.remove(old_contact) #удаляем старый
    old_contacts.append(contact)  # добавляем новый
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        ui_list = app.contact.get_contacts_list()  # список, загруженный через UI
        clean = app.contact.clean_contact() # очистка от лишних пробелов
        db_list = map(clean, db.get_contact_list())  # список, загруженный через БД
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
        print(ui_list)
        print(db_list)


#def test_modify_some_contact(app): #проверки из интерфейса
#    contact = Contact(firstname="Анна", lastname="Иванова", address="ул.Смольная, д.18", homephone="(495)123-12-23",
#                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20", secondaryphone="(495)1820",
#                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт
#    if app.contact.count() == 0:
#        app.contact.create(contact)
#    old_contacts = app.contact.get_contacts_list() # считываем старый список со страницы
#    index = randrange(len(old_contacts))
#    contact.id = old_contacts[index].id #добавляем недостающий id в объект типа контакт
#    app.contact.modify_contact_by_index(index, contact) # передаем объект в функцию модификации
#    new_contacts = app.contact.get_contacts_list() # считываем новый список со страницы
#    assert len(old_contacts) == app.contact.count()
#    old_contacts[index] = contact # меняем контакт в старом списке вручную
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

