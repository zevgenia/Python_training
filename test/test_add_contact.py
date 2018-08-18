# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact1(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname="Иван", middlename="Петрович", lastname="Сидоров"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_contact2(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname="Валентина", lastname="Петрова"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
