from model.group import Group
# from random import randrange
import random


def test_modify_group_name(app, db, check_ui): #модификация случайной группы- проверки из БД
    group = Group(name="Моя группа", header="Моя группа", footer="Моя группа") #значение, на  которое будем менять выбранную группу
    if len(db.get_group_list()) == 0: #предусловие
        app.group.create(group)
    old_groups = db.get_group_list() #читаем группы до модификации
    old_group = random.choice(old_groups) # выбираем случайную группу из старого списка групп
    group.id = old_group.id # меняем id у новой группы на тот, который есть у группы, кот.собираемся менять
    app.group.modify_group_by_id(old_group.id, group) #модифицируем у группы,выбранной по id, значения (имя, header,footer)
    new_groups = db.get_group_list()  #читаем группы после модификации
    old_groups.remove(old_group) #удаляем из списка старую группу
    old_groups.append(group) #добавляем новую группу
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        ui_list = app.group.get_groups_list()  # список, загруженный через UI##
        clean = app.group.clean_name()
        db_list = map(clean, db.get_group_list())  # список, загруженный через БД
        assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)

#def test_modify_group_name1(app): #модификация случайной группы - проверки из интерфейса
#    group = Group(name="Моя группа") #значение, на  которое будем менять выбранную группу
#    if app.group.count() == 0:
#        app.group.create(group)
#    old_groups = app.group.get_groups_list() #читаем старый список
#    index = randrange(len(old_groups)) #выбираем случайный индекс из количества групп
#    group.id = old_groups[index].id # меняем id у новой группы на тот, который есть у группы, кот.собираемся менять
#    app.group.modify_group_by_index(index, group) # модифицируем у группы,выбранной по индексу, значения (имя, header,footer)
#    new_groups = app.group.get_groups_list() #читаем новый список
#    assert len(old_groups) == app.group.count() #предварительная проверка совпадения длин списков
#    old_groups[index] = group # меняем в старом списке имя, header, footer
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

