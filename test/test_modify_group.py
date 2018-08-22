from model.group import Group
from random import randrange

def test_modify_group_name(app):
    group = Group(name="Моя группа")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_groups_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="Моя группа"))
#    app.group.modify_first_group(Group(header="New Header"))
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    old_groups = app.group.get_groups_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="Моя группа"))
#    app.group.modify_first_group(Group(footer="New Footer"))
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)

