from model.group import Group
from model.contact import Contact
import re
from copy import deepcopy


def test_group_list(app, db):
    ui_list = app.group.get_groups_list() # список, загруженный через UI

    def clean(group):
        return Group(id=group.id, name=(re.sub("\s{2,}", " ", group.name)).strip())
    db_list = map(clean, db.get_group_list())  # список, загруженный через БД
#    db_list = db.get_group_list()  # список, загруженный через БД
    list_ui = deepcopy(ui_list)
    list_db = deepcopy(db_list)
    print("\nafter_ui_list", list_ui)
    print("\nafter_db_list", list(list_db))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)



def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list() # список, загруженный через UI

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip())
    db_list = map(clean, db.get_contact_list())  # список, загруженный через БД
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)

