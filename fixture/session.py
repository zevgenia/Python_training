

# Помощник сессий, содержит вспомогательные методы, которые относятся к открытию/закрытию сессии
class SessionHelper:

    def __init__(self, app): # конструктор, в качестве параметра принимает ссылку на фикстуру
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page() # обращение к методу перехода на гл.страницу через фикстуру
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
#        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_xpath("//form[@name='logout']//a[.='Logout']").click()

    # метод проверяет что произошел выход из системы
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0 # мы в системе

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    # метод проверяет что произошел вход в систему под именем конкретного пользователя
    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)
