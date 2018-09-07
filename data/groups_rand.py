from model.group import Group
import random
import string

constant = [
    Group(name="Друзья", header="Друзья", footer="Друзья"),
    Group(name="Работа", header="Сослуживцы", footer="Сослуживцы")

]

def random_string(prefix, maxlen):  #генератор случайных строк, добавление пунктуации - string.punctuation
    simbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])


# тестовые данные генерируются с помощью генератора случайных строк
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(3)
]
