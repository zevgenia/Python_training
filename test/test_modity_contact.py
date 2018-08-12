from model.contact import Contact


def test_modify_first_contact1(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    app.contact.modify_first_contact(Contact(firstname="Анна", middlename="Ивановна", lastname="Иванова"))


def test_modify_first_contact2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Иван"))
    app.contact.modify_first_contact(Contact(lastname="Барто"))
