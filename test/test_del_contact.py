from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

