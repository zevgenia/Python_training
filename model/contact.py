
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.lastname == other.lastname