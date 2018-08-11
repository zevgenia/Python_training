

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
