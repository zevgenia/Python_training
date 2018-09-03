# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):  #генератор случайных строк
    simbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])

# тестовые данные - полный перебор комбинаций пустых и непустых значений для 3х полей - итого 8
testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    print(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

