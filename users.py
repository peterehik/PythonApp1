import random
from User import User
from datetime import datetime


def add_to_lookup(lookup, key, value):
    if isinstance(key, str):
        key = key.upper()
    if key in lookup:
        lookup[key].append(value)
    else:
        lookup[key] = [value]


def get_value_from_lookup(lookup, key):
    if isinstance(key, str):
        key = key.upper()
    if key in lookup:
        return lookup[key]
    return []


class UserGenerationLogic:

    _usersFilePath = "datasource/users.csv"
    _names = ['John', 'Mark', 'Dimitri', 'Noh', 'Benford', 'Ehikhuemen', 'Janice', 'Sarah', 'Wedeck', 'Smith',
              'Stannis', 'Simcoe', 'Dylan']
    _genders = ['male', 'female']
    _places = ['Los Angeles CA', 'Hong Kong', 'New York', 'Arlington TX', 'Washington VA', 'Madrid', 'Valencia',
               'London', 'Brooklyn NY']

    _allUsers = []
    _metadata_lookUp = {}
    _gender_lookUp = {}
    _fname_lookup = {}
    _lname_lookup = {}

    def __init__(self):
        with open(self._usersFilePath, 'r') as file:
            for line in file:
                print(line)

    def save_users_to_filesystem(self):
        with open(self._usersFilePath, 'w') as file:
            header = ','.join(['Id', 'First Name', 'Last Name', 'DOB',
                               'Metadata', 'Gender', 'Date Saved'])
            file.write(header + '\n')
            for user in self._allUsers:
                user_csv = ','.join(['"' + str(x) + '"' for x in [user.id, user.firstName, user.lastName,
                                     user.dob, user.metadata, user.gender, user.dateSaved]])
                print(user_csv)
                file.write(user_csv + '\n')

    def find_users(self, query):
        results = []
        if query in self._genders:
            results.extend(get_value_from_lookup(self._gender_lookUp, query))
        else:
            results.extend(get_value_from_lookup(self._fname_lookup, query))
            results.extend(get_value_from_lookup(self._lname_lookup, query))

        if len(results) == 0:
            results.extend(get_value_from_lookup(self._metadata_lookUp, query))

        return results

    def save_user_to_memory(self, user):
        self._allUsers.append(user)
        add_to_lookup(self._gender_lookUp, user.gender, user)
        add_to_lookup(self._fname_lookup, user.firstName, user)
        add_to_lookup(self._lname_lookup, user.lastName, user)
        metadata_keys = user.metadata.split(', ')
        for key in metadata_keys:
            add_to_lookup(self._metadata_lookUp, key, user)

    def create_user(self, user):
        user.id = len(self._allUsers) + 1
        user.dateSaved = str(datetime.now())
        self.save_user_to_memory(user)

    def create_random_users(self, num):
        assert isinstance(num, int)
        for i in range(0, num):
            entity = {"dateSaved": '',
                      "firstName": random.choice(self._names),
                      "lastName": random.choice(self._names),
                      "gender": random.choice(self._genders)}
            age = random.randint(1, 80)
            entity["dob"] = '{}/{}/{}'.format(random.randint(1, 12), random.randint(1, 30), random.randint(1920, 2016))
            entity["metadata"] = '{} {}, age {}, {}, {}'.format(entity["firstName"], entity["lastName"], age,
                                                                random.choice(self._genders),
                                                                random.choice(self._places))
            user_entity = User(entity)
            self.create_user(user_entity)
            yield user_entity
