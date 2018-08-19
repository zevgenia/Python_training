from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contacts_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
