# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact1(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Иван", middlename="Петрович", lastname="Сидоров")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print("\nold_contacts", old_contacts)
    print("new_contacts", new_contacts)


#def test_add_contact2(app):
#    old_contacts = app.contact.get_contacts_list()
#    contact = Contact(firstname="Валентина", lastname="Петрова")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contacts_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)