# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Applicaton


@pytest.fixture()
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Иван", middlename="Петрович", lastname="Сидоров"))
    app.logout()
