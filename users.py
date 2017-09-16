import random
from User import User

from datetime import datetime


def add_to_lookup(lookup, key, value):
    if key in lookup:
        lookup[key].append(value)
    else:
        lookup[key] = [value]


def get_value_from_lookup(lookup, key):
    if key in lookup:
        return lookup[key]
    return []


class UserGenerationLogic:
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

    def create_user(self, user):
        user.dateSaved = str(datetime.now())
        self._allUsers.append(user)
        add_to_lookup(self._gender_lookUp, user.gender, user)
        add_to_lookup(self._fname_lookup, user.firstName, user)
        add_to_lookup(self._lname_lookup, user.lastName, user)
        metadata_keys = user.metadata.split(', ')
        for key in metadata_keys:
            add_to_lookup(self._metadata_lookUp, key, user)

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
