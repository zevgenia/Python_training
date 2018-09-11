from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(db.get_contact_list())
    old_contacts.remove(contact)  # из списка будет удален элемент, равный заданному
    assert old_contacts == new_contacts
    if check_ui:
        ui_list = app.contact.get_contacts_list()  # список, загруженный через UI
        clean = app.contact.clean_contact()
        db_list = map(clean, db.get_contact_list())  # список, загруженный через БД
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)

