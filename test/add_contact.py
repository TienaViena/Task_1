# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(name="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Erast", lastname="Fandorin", nickname="Juffin Hally", company="Adventures", mobile="+79991112233",
                               email="JuffinHally@yandex.ru", bday="14", bmonth="July", byears="1996"))
    app.session.logout()