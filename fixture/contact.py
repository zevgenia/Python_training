from model.contact import Contact


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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        # select first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.go_to_home_page()
        self.contact_cash = None

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
        if not (wd.current_url.endswith("/index.php") and wd.find_element_by_xpath("//div[@id='search-az']/form/input")):
            wd.find_element_by_xpath("//div[@id='nav']//a[.='home']").click()

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
            for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                self.contact_cash.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cash)

