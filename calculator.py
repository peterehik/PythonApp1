import json


class BaseClass:

    def json_serialize(self):
        return json.dumps(self.__dict__)

    def json_deserialize(self, j):
        self.__dict__ = json.loads(j)


class Person(BaseClass):
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: {}\r\nAge: {}'.format(self.name, self.age);


person = Person('Jason Bourne', 25)
personSerial = person.json_serialize()
print(personSerial)

anotherPerson = Person()
anotherPerson.json_deserialize(personSerial)
print(anotherPerson)

