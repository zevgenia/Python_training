from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Анна", middlename="Ивановна", lastname="Иванова"))
