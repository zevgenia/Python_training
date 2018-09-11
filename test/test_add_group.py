# -*- coding: utf-8 -*-
from model.group import Group
from copy import deepcopy


def test_add_group(app, db, json_groups): #json_groups загрузка из json-файла
    group = json_groups
    old_groups = db.get_group_list() # получаем старый список групп из бд
    app.group.create(group) # создаем новую группу с полученными параметрами
    new_groups = db.get_group_list() # получаем новый список из бд
    old_groups.append(group) #добавляем группу в список вручную
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

