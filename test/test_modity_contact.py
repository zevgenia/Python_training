from model.contact import Contact


def test_modify_first_contact1(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Анна", middlename="Ивановна", lastname="Иванова")
    contact.id = old_contacts[0].id #добаляем недостающий id
    if app.contact.count() == 0:
        app.contact.create(contact)
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact # меняем контакт вручную
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print("old_contacts", old_contacts)
    print("new_contacts", new_contacts)


#def test_modify_first_contact2(app):
#    old_contacts = app.contact.get_contacts_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Иван"))
#    app.contact.modify_first_contact(Contact(lastname="Барто"))
#    new_contacts = app.contact.get_contacts_list()
#    assert len(old_contacts) == len(new_contacts)