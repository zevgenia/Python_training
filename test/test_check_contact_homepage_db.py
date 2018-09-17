from model.contact import Contact
import re
from random import randrange


def test_check_contact_between_home_page_db(app, db):
    contact = Contact(firstname="Анна", lastname="Иванова", address="ул.Бабушкина, д.18", homephone="(495)123-12-23",
                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20",
                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    contacts_from_home_page = app.contact.get_contacts_list() # информация о контактах с гл.страницы
    contacts_from_db = db.get_contact_list() #информация о контакте из бд
    merged_contacts_from_db = merge_contacts_from_db(contacts_from_db)
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(merged_contacts_from_db, key=Contact.id_or_max)


def merge_contacts_from_db(contacts):
    def merge(contact):
        return Contact(id=str(contact.id), firstname=clean(contact.firstname), lastname=clean(contact.lastname),
                       address=clean(contact.address),
                       all_phones_from_home_page=merge_phones_like_from_home_page(contact.homephone,
                                                                                  contact.mobilephone,
                                                                                  contact.workphone,
                                                                                  contact.secondaryphone),
                       all_emails_from_home_page=merge_emails_like_from_home_page(contact.email,
                                                                                  contact.email2,
                                                                                  contact.email3))

    return list(map(merge, contacts))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_from_home_page(homephone,mobilephone,workphone,secondaryphone):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [homephone, mobilephone, workphone, secondaryphone]))))


def merge_emails_like_from_home_page(email, email2, email3):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,[email, email2, email3])))


def clean(contact):
    contact = re.sub("\s{2,}", " ", contact)  # заменяем множественные пробелы (от 2х) на 1 пробел
    contact = contact.strip()  # убираем пробел в начале и в конце
    return contact