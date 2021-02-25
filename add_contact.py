# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(name="admin", password="secret")
    app.create_contact(Contact(firstname="Erast", lastname="Fandorin", nickname="Juffin Hally", company="Adventures", mobile="+79991112233",
                               email="JuffinHally@yandex.ru", bday="14", bmonth="July", byears="1996"))
    app.logout()