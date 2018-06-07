# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Vasya", middle_name="Ivanovich", last_name="Petrov", nickname="Bublik",
                               title="Title", company="IVI", address="Petrovskaya, 33", home_tel="7777777", mobile_tel="8878787",
                               work_tel="3434332", fax="4635463", e_mail="bublik@mail.ru", homepage="bublik.com", birthday="1986",
                               anniversary="2000", secondary_address="Mayskaya, 3", home="Home", notes="Moy kontakt")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(first_name="", middle_name="", last_name="", nickname="",
#                                title="", company="", address="", home_tel="", mobile_tel="",
#                                work_tel="", fax="", e_mail="", homepage="", birthday="",
#                                anniversary="", secondary_address="", home="", notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)