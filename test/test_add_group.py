# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Applicaton


@pytest.fixture()
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="newGroup", header="my group", footer="mygroup"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

