# -*- coding: utf-8 -*-


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(first_name="New name")
    app.session.logout()
