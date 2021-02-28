# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(name="admin", password="secret")
    app.contact.create(Contact(firstname="Erast", lastname="Fandorin", nickname="Juffin Hally", company="Adventures", mobile="+79991112233",
                               email="JuffinHally@yandex.ru", bday="14", bmonth="July", byears="1996"))
    app.session.logout()