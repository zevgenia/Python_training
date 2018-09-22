from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re
import time

# Помощник контактов, содержит все вспомогательные методы, которые относятся к работе с контактами
class ContactHelper:

    def __init__(self, app): # конструктор, в качестве параметра принимает ссылку на фикстуру
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.go_to_home_page()
        self.contact_cash = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        # submit delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()
        self.contact_cash = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id)
        # submit delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()
        self.contact_cash = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index) # click on checkbox
        self.open_contact_to_edit_by_index(index)  # click on pencil
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.go_to_home_page()
        self.contact_cash = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id) # click on checkbox
        self.open_contact_to_edit_by_id(id)  # click on pencil
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.go_to_home_page()
        self.contact_cash = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_value('%s' % id)
        wd.find_element_by_name("add").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("phone2", contact.secondaryphone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    # посчитать сколько чек-боксов на странице
    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    # получение списка контактов со страницы
    def get_contacts_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cash.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                 all_phones_from_home_page=all_phones, address=address,
                                                 all_emails_from_home_page=all_emails))
        return list(self.contact_cash)

    # откытие страницы редактирования контакта - index
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click() # click on pencil

    # откытие страницы редактирования контакта - id
    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, address=address, email=email,
                       email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text)
        if homephone is not None:
            homephone = re.search("H: (.*)", text).group(1)  # первая часть, до перевода строки
        mobilephone = re.search("M: (.*)", text)
        if mobilephone is not None:
            mobilephone = re.search("M: (.*)", text).group(1)  # первая часть, до перевода строки
        workphone = re.search("W: (.*)", text)
        if workphone is not None:
             workphone = re.search("W: (.*)", text).group(1)  # первая часть, до перевода строки
        secondaryphone = re.search("P: (.+)", text)
        if secondaryphone is not None:
            secondaryphone = re.search("P: (.+)", text).group(1)# первая часть, до перевода строки
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def clean_contact(self):
        def clean(contact):
            return Contact(id=contact.id, firstname=(re.sub("\s{2,}", " ", contact.firstname)).strip(),
                           lastname=(re.sub("\s{2,}", " ", contact.lastname)).strip(),
                           address=(re.sub("\s{2,}", " ", contact.address)).strip(),
                           email=(re.sub("\s{2,}", " ", contact.email)).strip(),
                           mobilephone=(re.sub("\s{2,}", " ", contact.mobilephone)).strip())

        return clean

    def add_contact_to_group_by_id(self, group_id, contact_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.go_to_home_page_all_contacts()
        self.select_contact_by_id(contact_id)
        self.select_group_by_id(group_id)
        self.return_to_groups_page(group_id)
        self.go_to_home_page_all_contacts()

    def return_to_groups_page(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='msgbox']//a[@href='./?group=%s']" % id).click()

    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and wd.find_element_by_xpath("//div[@id='search-az']/form/input")):
            wd.find_element_by_xpath("//div[@id='nav']//a[.='home']").click()

    def go_to_home_page_all_contacts(self):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("group"))
        select.select_by_visible_text('[all]')

    def del_contact_from_group_by_id(self, group_id, contact_id):
        wd = self.app.wd
        self.go_to_group_page(group_id)
        self.select_contact_by_id(contact_id)
        self.del_contact_from_group(group_id)
        self.return_to_groups_page(group_id)
        self.go_to_home_page_all_contacts()

    def go_to_group_page(self, id):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("group"))
        select.select_by_value("%s" % id)

    def del_contact_from_group(self, id):
        wd = self.app.wd
        # submit remove
        wd.find_element_by_name("remove").click()
