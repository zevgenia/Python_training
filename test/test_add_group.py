# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import testdata as testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_groups_list() #получаем список со страницы
    app.group.create(group) #создаем новую группу с полученными параметрами
    new_groups = app.group.get_groups_list() # получаем новый список со страницы
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    print("\nold_contacts", old_groups)
    print("new_contacts", new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

