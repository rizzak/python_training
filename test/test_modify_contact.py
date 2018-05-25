# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Vasya"))
    app.contact.modify_first_contact(Contact(first_name="New name"))
