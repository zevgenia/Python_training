import json
import pytest
from fixture.application import Application
import importlib
import jsonpickle

fixture = None
target = None
import os.path


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is not None:
        if fixture.is_valid():  # фикстура хорошая
            return fixture
    #print("создаем fixture", fixture)
    fixture = Application(browser=browser, base_url=target["baseURL"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
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
    parser.addoption("--target", action="store", default="target.json")


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
