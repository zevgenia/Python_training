#import pymysql.cursors
import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    # конструктор фикстуры
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
#        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self): # загружает информацию о группах из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self): # загружает информацию о контактах из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3"
                           " from addressbook WHERE deprecated = '0000-00-00'")
            for row in cursor.fetchall():
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, secondaryphone=phone2,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()