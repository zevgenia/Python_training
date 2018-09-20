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
    #выбираем случайный контакт и случайную группу
    contacts_list = db.get_contact_list()  #получаем список контактов
    cont = random.choice(contacts_list)
    groups_list = db.get_group_list() #получаем список групп
    contacts_in_group_old, group = match_contact_to_group(app, cont, groups_list, orm)
    contacts_in_group_new = orm.get_contacts_in_group(group.id)
    assert sorted(contacts_in_group_old, key=Contact.id_or_max) == sorted(contacts_in_group_new, key=Contact.id_or_max)


def match_contact_to_group(app, cont, groups_list, orm):
    contacts_in_group_old = []
    for group in groups_list:
        try:
            l = orm.get_contacts_not_in_group(
                Group(id=group.id))  # провекряем какие контакты еще не входят в эту группу
            if cont in l:
                print("подошли контакт и группа", cont.id, group.id)
                contacts_in_group_old = orm.get_contacts_in_group(
                    Group(id=group.id))  # получаем старый список контактов в группе
                app.contact.add_contact_to_group_by_id(group.id, cont.id)  # добавляем контакт в группу
                return (contacts_in_group_old, group)
                break
        finally:
            pass  # db.destroy()
    return contacts_in_group_old, cont.id, group.id