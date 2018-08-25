from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, homephone=None, mobilephpone=None,
                 workphone=None, secondaryphone=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephpone = mobilephpone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and \
               (self.lastname == other.lastname and self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
