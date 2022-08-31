from copy import deepcopy
from pprint import pprint

#
# 1. Recap
#

# str, str format
name = 'Goncalo'  # "" or '' is same
hello_message = "Hello, %s!" % name  # legacy

print(hello_message)

hello_message = f'Hello, {name}!'  # more readable

print(f'Hello, {name}!')

print(f'1 + 1 = {1+1}')
result = 1 + 1
print(f'{result = }')
print(f'{hello_message = }')

# int
number = 1 + 2*4 - -10 - 30
print(number, type(number))

# float
number = 2.2
print(number, type(number))
# look how number type was changed

# bool
some_bool = True
is_1 = number == 1
print(is_1)
none = None

# até agora foram tipos primitivos
# list
my_list = [1, 2, 3, 4, 10]
print(sum(my_list) == 20)
my_list.append(1)
my_list.extend([1, 2, 3, 4])
my_list.insert(1, 1)
print(my_list, my_list[1])
print(my_list[:4])
print(my_list[:-1])

# tuple
my_tuple = ("Goncalo", "software dev", 25)
# try my_tuple[1] = "aerospace eng."
# it cannot be changed! But, if it stores an address...
some_list = [1, 2, 3]
another_tuple = ("Hello!", 12, some_list)
print(another_tuple)
some_list.append(4)
print(another_tuple)
another_tuple[2].reverse()
print(another_tuple, type(another_tuple))
name, job, age = my_tuple

# dict
dictionary = {'name': 'Goncalo', 'job': 'software-dev', 'age': 25}
print(dictionary, type(dictionary))
pprint(dictionary)
dictionary['age'] = 50
pprint(dictionary)
dictionary['kids'] = 2
print(dictionary.values(), dictionary.keys(), dictionary.items())

for key, value in dictionary.items():  # tup first
    if isinstance(value, str):
        print(f'{key=}, {value=}')

# Nota: copy deepcopy
same_dict = dictionary
same_dict['name'] = 'Pedro'
print(dictionary)
other_dict = deepcopy(dictionary)
other_dict['name'] = 'Joao'
print(dictionary)

#
# 2. Dicts e sets, hash tables
#
# Each key is hashed and stored for fast lookup
# No key repetition
# Sets are the same, but keys are values

my_set = {1, 2, "hello"}
print(my_set)
my_set.update({1, 2, 3, 4})
print(my_set)
print(set([1, 1, 1, 2, 3, 1, 4, 4, 5, 3]))
# try my_set[0] --> indexing does not work

#
# 3. Collections
#
# see collections. --

###### OrderedDict
#####ordered_dict = collections.OrderedDict()
#####ordered_dict['name'] = 'Gonçalo'
#####ordered_dict['age'] = 25
#####pprint(ordered_dict)
#####ordered_dict.setdefault('kids', 2)
#####pprint(ordered_dict['kids'])
#####
###### defaultdict
#####kids_per_person = collections.defaultdict(list)
#####pprint(kids_per_person)
#####print(kids_per_person['John'])
#####kids_per_person['Gonçalo'] = ['Rosarinho', 'Luis']
#####pprint(kids_per_person)
#####kids_per_person['Maria'].append('some_name')
#####pprint(dict(kids_per_person))
#####
#######
###### namedtuple
#####Person = collections.namedtuple('Person', ['name', 'age', 'job'])
#####goncalo = Person('Goncalo', 25, 'soft.dev.')
#####pprint(goncalo)
#####print(goncalo.name, goncalo.age, goncalo.job)  # more readable tuple!
#####pprint(goncalo[0])
###### comparison
#####persons = [('g', 25, 'soft.dev'), ('j', 30, 'eng'), ('m', 30, 'med')]
#####pprint(persons)
#####
#####persons = [
#####    Person(name='g', age=25, job='soft.dev'),
#####    Person('j', 30, 'eng'),
#####    Person('m', 30, 'med')
#####]
#####
#####pprint(persons)
#####for person in persons:
#####    print(f'{person.name} is {person.age} years old')
#####    # print(f'{person[0]} is {person[1]} years old')
#####
###### If there's time, deque
#####my_deq = collections.deque([1, 2, 3])
#####print(my_deq.popleft())
#####my_deq.appendleft('ace')
#####my_deq.append(4)
#####my_deq.extend([5, 6, 7])
#####print(my_deq.pop())
#####pprint(my_deq)

#
# 4. Classes
#


class Person:
    def __init__(self, name: str, age: int, job: str, kids: list) -> None:
        self.name = name
        self.age = age
        self.job = job
        self.kids = kids

    def has_kids(self) -> bool:
        return len(self.kids) > 0

    def last_name(self) -> str:
        names = self.name.split(' ')
        if len(names) > 1:
            return names[-1]
        else:
            return ''


goncalo = Person('Gon', 25, 'dev', ['R', 'L'])
if goncalo.has_kids():
    pprint(goncalo.kids)
print(goncalo.last_name())
goncalo.name = 'Goncalo Magalhaes'
print(goncalo.last_name())
print(goncalo)
