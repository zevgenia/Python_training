

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

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        self.go_to_home_page()
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        # select first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.go_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.find_element_by_name("searchstring")):
            wd.find_element_by_xpath("//div[@id='nav']//a[.='home']").click()

    # посчитать сколько чек-боксов на странице
    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))