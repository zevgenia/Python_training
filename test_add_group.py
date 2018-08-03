# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Applicaton


@pytest.fixture()
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="newGroup", header="my group", footer="mygroup"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

