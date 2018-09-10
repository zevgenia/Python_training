import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    # конструктор фикстуры
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self): # загружает информацию о группах из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self): # загружает информацию о контактах из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, email from addressbook "
                           "WHERE deprecated = '0000-00-00'")
            for row in cursor.fetchall():
                (id, firstname, lastname, address, mobile, email) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    mobilephone=mobile, email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()