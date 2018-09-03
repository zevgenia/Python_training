# -*- coding: utf-8 -*-
from model.group import Group
import pytest

testdata = [
    Group(name="newGroup", header="my group", footer="mygroup"),
    Group(name="", header="", footer="")
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):

    old_groups = app.group.get_groups_list()
    app.group.create(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

