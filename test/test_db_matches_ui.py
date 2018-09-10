from model.group import Group
from model.contact import Contact

def test_group_list(app, db):
    ui_list = app.group.get_group_list() # список, загруженный через UI

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())  # список, загруженный через БД
    print("\nui_list", ui_list)
    print("\ndb_list", db_list)
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list() # список, загруженный через UI

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip())
    db_list = map(clean, db.get_contact_list())  # список, загруженный через БД
    print("\nui_list", ui_list)
    print("\ndb_list", db_list)
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)

