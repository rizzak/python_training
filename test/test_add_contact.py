# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                    home_tel="", mobile_tel="", work_tel="", fax="", email="", homepage="", birthday="",
                    anniversary="", secondary_address="", secondary_tel="", notes="")] + [
    Contact(first_name=random_string('first_name', 10), middle_name=random_string('middle_name', 10), last_name=random_string('last_name', 10),
            nickname=random_string('nickname', 10), title=random_string('random_string', 10), company=random_string('company', 10),
            address=random_string('address', 10), home_tel=random_string('home_tel', 10), mobile_tel=random_string('mobile_tel', 10),
            work_tel=random_string('work_tel', 10), fax=random_string('fax', 10), email=random_string('email', 10),
            homepage=random_string('homepage', 10), birthday=random_string('birthday', 10), anniversary=random_string('anniversary', 10),
            secondary_address=random_string('secondary_address', 10), secondary_tel=random_string('secondary_tel', 10), notes=random_string('notes', 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(first_name="", middle_name="", last_name="", nickname="",
#                                title="", company="", address="", home_tel="", mobile_tel="",
#                                work_tel="", fax="", email="", homepage="", birthday="",
#                                anniversary="", secondary_address="", home="", notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)