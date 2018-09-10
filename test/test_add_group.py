# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups): #json_groups загрузка из json-файла
    group = json_groups
    old_groups = db.get_group_list() #получаем список со страницы
    app.group.create(group) #создаем новую группу с полученными параметрами
    new_groups = db.get_group_list() # получаем новый список со страницы
    old_groups.append(group)
    print("\nold_groups", old_groups)
    print("new_groups", new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

