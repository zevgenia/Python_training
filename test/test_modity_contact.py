from model.contact import Contact


def test_modify_first_contact1(app):
    old_contacts = app.contact.get_contacts_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    app.contact.modify_first_contact(Contact(firstname="Анна", middlename="Ивановна", lastname="Иванова"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_first_contact2(app):
    old_contacts = app.contact.get_contacts_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    app.contact.modify_first_contact(Contact(lastname="Барто"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)