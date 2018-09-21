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
    groups_list_old = []
    group_id = 0
    cont_id = 0
    global status
    status = False
    while status is False:
        cont = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
        if cont in contacts_not_in_group:
            group_id = group.id
            cont_id = cont.id
            groups_list_old = orm.get_contacts_not_in_group(Group(id=group.id))
            for item in groups_list_old:
                print("этого контакта", item.id, "нет в группе", group_id, group.name)
            app.contact.add_contact_to_group_by_id(group.id, cont.id)
            print("добавляем контакт", cont_id, " в группу",  group_id, group.name)
            groups_list_new = orm.get_contacts_in_group(Group(id=group.id))
            print("теперь в группе", group.id, "находятся контакты")
            for item in groups_list_new:
                print(item)
            return (groups_list_old, cont_id, group_id, )
            status = True
            #break
        print("продолжаем выбирать")
        continue

    print("вернули id контакта и группы, старый список контактов в группу", groups_list_old, cont_id, group_id, )

    groups_list_new = orm.get_contacts_in_group(Group(id=group_id))
    if cont_id in groups_list_new:
            print("группа добавлена")
#    assert sorted(groups_list_old, key=Contact.id_or_max) == sorted(groups_list_new, key=Contact.id_or_max)


