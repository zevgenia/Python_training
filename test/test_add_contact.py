# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacs_rand import testdata as testdata


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    print("\nold_contacts", old_contacts)
    print("new_contacts", new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


