
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
    fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout() #если мы еще в системе, на странице есть ссылка logout
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

