# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="newGroup", header="my group", footer="mygroup"))


def test_add_empty_group(app):
    app.group.create(Group(name="Empty group"))
