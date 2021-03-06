import json
import pytest
from fixture.application import Application
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture
import os.path

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is not None:
        if fixture.is_valid():  # фикстура хорошая
            return fixture
    #print("создаем fixture", fixture)
    fixture = Application(browser=browser, base_url=web_config["baseURL"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session") #инициализируем фикстуру в начале сессии
def db(request): # метод для инициализации фикстуры
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session") #инициализируем фикстуру в начале сессии
def orm(request): # метод для инициализации фикстуры
    orm_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=orm_config['host'], name=orm_config['name'], user=orm_config['user'],
                          password=orm_config['password'])
    def fin():
        pass #ormfixture.destroy()
    request.addfinalizer(fin)
    return ormfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout() #если мы еще в системе, на странице есть ссылка logout
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module): # data_groups_const - загрузка из модуля c постоянными данными
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file): # json_groups - загрузка из json-файла
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
