from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


# Класс-менеджер, который инициализирует всех помощников
class Application:

    # создание фикстуры, инициализация драйвера
    def __init__(self):
        # self.wd = WebDriver()
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        # конструирование помощников, передаем ссылку на саму фикстуру
        self.session = SessionHelper(self)# помощник сесссий получает ссылку на объект класса Application
        self.group = GroupHelper(self)# помощник групп получает ссылку на объект класса Application
        self.contact = ContactHelper(self)# помощник контактов получает ссылку на объект класса Application

    def open_home_page(self): # метод навигации, кандидат на перенос в соответ.помощник
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # метод разрушает фикстуру, останавливает браузер
    def destroy(self):
        self.wd.quit()

