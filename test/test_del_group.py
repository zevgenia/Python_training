from model.group import Group
import random
import re


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Моя группа"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group) #из списка будет удален элемент, равный заданному
    assert old_groups == new_groups
    if check_ui:
        ui_list = app.group.get_groups_list()  # список, загруженный через UI

        def clean(group):
            return Group(id=group.id, name=(re.sub("\s{2,}", " ", group.name)).strip())
        db_list = map(clean, db.get_group_list())  # список, загруженный через БД
        assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)
