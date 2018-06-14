# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_name(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Vasya"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact = Contact(first_name="New name")
    modified_contact.id = contact.id
    app.contact.modify_contact_by_id(modified_contact.id, modified_contact)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(contact)
    old_contacts[index] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
