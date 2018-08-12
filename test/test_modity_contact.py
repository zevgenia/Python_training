from model.contact import Contact


def test_modify_first_contact1(app):
    app.contact.modify_first_contact(Contact(firstname="Анна", middlename="Ивановна", lastname="Иванова"))


def test_modify_first_contact2(app):
    app.contact.modify_first_contact(Contact(lastname="Барто"))