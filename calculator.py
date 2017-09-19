from users import UserGenerationLogic


def prompt_user_for_number(prompt, min_val=1, max_val=1000):
    number = input(prompt)
    if number.isdigit() and min_val <= int(number) <= max_val:
        return int(number)
    if not(number.isdigit()):
        print('You have to enter an integer')
    else:
        print('You have to enter an integer between 0 and 1000')
    return prompt_user_for_number(prompt)


def prompt_user_for_search(prompt):
    query = input(prompt)
    users = _userLogic.find_users(query)
    print_users(users)
    if input('Keep playing?: ') in ['Y', 'Yes']:
        prompt_user_for_search(prompt)


def print_users(users):
    for user in users:
        print(user.toJSON())


num_users = prompt_user_for_number('Generate x number of users where 1 <= x <= 1000, x: ')
_userLogic = UserGenerationLogic()
generated_users = _userLogic.create_random_users(num_users)
if input('View Generated Users?: ').upper() in ['Y', 'YES']:
    print_users(generated_users)

prompt_user_for_search('Find User: ')
_userLogic.save_users_to_filesystem()
input()


# class Person(BaseClass):
#     def __init__(self, name='', age=0):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return 'Name: {}\r\nAge: {}'.format(self.name, self.age)
#
#
# person = Person('Jason Bourne', 25)
# personSerial = person.json_serialize()
# print(personSerial)
#
# anotherPerson = Person()
# anotherPerson.json_deserialize(personSerial)
# print(anotherPerson)

