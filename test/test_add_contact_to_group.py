from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db, orm):
    #проверка - есть ли контакты
    contact = Contact(firstname="Анна", lastname="Иванова", address="ул.Смольная, д.18", homephone="(495)123-12-23",
                      mobilephone="903-456-12-12", workphone="+7(495)120 18 20", secondaryphone="(495)1820",
                      email="rrr@nai.ru", email2="qqq@ya.ru", email3="ttt@erf.org")# создаем объект контакт
    if len(db.get_contact_list()) == 0: #Если нет, добавить контакт
        app.contact.create(contact)
    #проверка есть ли группы
    if len(db.get_group_list()) == 0: #Если нет, добавить группу
        app.group.create(Group(name="Моя группа"))
    status = False
    while status False
        cont = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
        if cont in contacts_not_in_group:
            groups_list_old = len(orm.get_contacts_not_in_group(Group(id=group.id)))
            app.contact.add_contact_to_group_by_id(group.id, cont.id)
            groups_list_new = len(orm.get_contacts_not_in_group(Group(id=group.id)))
            print("группа", group.id)
            print("\ngroups_list_old", groups_list_old)
            print("\ngroups_list_new", groups_list_new)
            status = True
        else:
            print("надо выбрать новый контакт")
    print("группа", group.id)
    print("\ngroups_list_old", groups_list_old)
    print("\ngroups_list_new", groups_list_new)
#    assert sorted(groups_list_old, key=Contact.id_or_max) == sorted(groups_list_new, key=Contact.id_or_max)


