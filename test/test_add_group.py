# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):  #генератор случайных строк, добавление пунктуации - string.punctuation
    simbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


# тестовые данные генерируются с помощью генератора случайных строк
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(3)
]


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

