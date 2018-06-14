from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        # init_contact_creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # Возвращаемся на главную
        self.app.return_to_home_page()
        # Ждем возврата на главную страницу
        wd.find_element_by_id('search_count')
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_tel)
        self.change_field_value("mobile", contact.mobile_tel)
        self.change_field_value("work", contact.work_tel)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").click()

        self.change_field_value("byear", contact.birthday)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").click()

        self.change_field_value("ayear", contact.anniversary)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondary_tel)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click edit element
        wd.find_elements_by_css_selector('[alt="Edit"]')[index].click()
        # edit contact name
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector('[name="update"]').click()
        # Возвращаемся на главную
        self.app.return_to_home_page()
        # Ждем возврата на главную страницу
        wd.find_element_by_id('search_count')
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_edit_page_by_id(id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector('[name="update"]').click()
        # Возвращаемся на главную
        self.app.return_to_home_page()
        # Ждем возврата на главную страницу
        wd.find_element_by_id('search_count')
        self.contact_cache = None

    def open_edit_page_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        contact = wd.find_element_by_xpath(".//input[@id='%s']/../.." % id)
        contact.find_element_by_xpath(".//td[8]/a/img").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector('input[value=Delete]').click()
        # accept alert deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector('input[value=Delete]').click()
        # accept alert deletion
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_tel = wd.find_element_by_name("home").get_attribute("value")
        work_tel = wd.find_element_by_name("work").get_attribute("value")
        mobile_tel = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_tel = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, first_name=first_name, last_name=last_name, home_tel=home_tel, work_tel=work_tel,
                       mobile_tel=mobile_tel, secondary_tel=secondary_tel, address=address, email=email, email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_tel = re.search("H: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        mobile_tel = re.search("M: (.*)", text).group(1)
        secondary_tel = re.search("P: (.*)", text).group(1)
        return Contact(home_tel=home_tel, work_tel=work_tel,
                       mobile_tel=mobile_tel, secondary_tel=secondary_tel)