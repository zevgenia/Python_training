# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="newGroup", header="my group", footer="mygroup"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="Empty group"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)