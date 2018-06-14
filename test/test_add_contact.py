# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts):
    old_contacts = db.get_contact_list()
    app.contact.create(json_contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
