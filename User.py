from pythonapp1 import BaseClass


class User(BaseClass):

    def __init__(self, user):
        self.id = 0
        self.firstName = user["firstName"]
        self.lastName = user["lastName"]
        self.dob = user["dob"]
        self.metadata = user["metadata"]
        self.gender = user["gender"]
        self.dateSaved = user["dateSaved"]

