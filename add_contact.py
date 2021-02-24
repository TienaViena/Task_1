# -*- coding: utf-8 -*-
import pytest
from group_contact import Group_contact
from application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Group_contact(firstname="Erast", lastname="Fandorin", nickname="Juffin Hally", company="Adventures", mobile="+79991112233",
                        email="JuffinHally@yandex.ru", bday="14", bmonth="July", byears="1996"))
    app.logout()