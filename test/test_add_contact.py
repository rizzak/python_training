# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Vasya", middle_name="Ivanovich", last_name="Petrov", nickname="Bublik",
                   title="Title", company="IVI", address="Petrovskaya, 33", home_tel="7777777", mobile_tel="8878787",
                   work_tel="3434332", fax="4635463", e_mail="bublik@mail.ru", homepage="bublik.com", birthday="1986",
                   anniversary="2000", secondary_address="Mayskaya, 3", home="Home", notes="Moy kontakt"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nickname="",
                   title="", company="", address="", home_tel="", mobile_tel="",
                   work_tel="", fax="", e_mail="", homepage="", birthday="",
                   anniversary="", secondary_address="", home="", notes=""))
    app.session.logout()