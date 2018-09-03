from model.contact import Contact
import re
from random import randrange


def test_check_contact_between_home_page_edit_page(app):
    contact = Contact(firstname="Анна", lastname="Иванова", address="ул.Бабушкина, д.18", homephone="(495)123-12-23",
                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20",
                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт
    list_contacts = app.contact.count()
    if list_contacts == 0:
        app.contact.create(contact)
    index = randrange(list_contacts)
    contact_from_home_page = app.contact.get_contacts_list()[index] # информация о контакте с гл.страницы
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)#информация о контакте с edit page
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_from_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравнение телефонов объединенным куском с view page и объединенным куском с edit page
    assert merge_phones_like_from_home_page(contact_from_view_page) == merge_phones_like_from_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3])))