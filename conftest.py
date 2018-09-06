
import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is not None:
        if fixture.is_valid(): #фикстура хорошая
#            print("fixture хорошая", fixture)
            return fixture
#        print("fixture испортилась", fixture)
#    print("создаем fixture", fixture)
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseURL")
    fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout() #если мы еще в системе, на странице есть ссылка logout
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")

