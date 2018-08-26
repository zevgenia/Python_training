import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0] # информация о контакте с гл.страницы
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)#информация о контакте с edit page
    # Сравнение телефонов "одним куском" с home page и объединенным куском с edit page
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравнение телефонов объединенным куском с view page и объединенным куском с edit page
    assert merge_phones_like_from_home_page(contact_from_view_page)== merge_phones_like_from_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,contact.secondaryphone]))))

