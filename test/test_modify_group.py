from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Моя группа"))
    app.group.modify_first_group(Group(name="New Group"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Моя группа"))
    app.group.modify_first_group(Group(header="New Header"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    old_groups = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Моя группа"))
    app.group.modify_first_group(Group(footer="New Footer"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)

