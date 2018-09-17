import pymysql.cursors
#import mysql.connector
#from fixture.db import DbFixture
from fixture.orm import ORMFixture

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()

