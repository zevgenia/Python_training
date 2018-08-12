# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact1(app):
    app.contact.create(Contact(firstname="Иван", middlename="Петрович", lastname="Сидоров"))


def test_add_contact2(app):
    app.contact.create(Contact(firstname="Валентина", lastname="Петрова"))