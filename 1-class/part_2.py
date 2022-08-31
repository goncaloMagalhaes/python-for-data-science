import collections
from pprint import pprint
from typing import List, Generator
from sys import getsizeof
import itertools

# range
print(my_range := range(10), type(my_range))
print(list(my_range))
print(list(range(2, 30, 3)))

sum_all = 0
for i in range(10):
    sum_all += i
    print(sum_all, end=' ')
# equivalent of C's for (int i=0; i<10, i++)
print('\n')

for _ in range(3):
    print('heep heep hurray!')

# lambdas


def greet(name: str) -> str:
    # 1-liner can become a lambda
    return f'Howdy, {name}!'


print(greet('Joao'))

# lambda_greet = lambda name: f'Howdy, {name}!'
# print(lambda_greet('Maria'))

# another lambda example
Person = collections.namedtuple('Person', ['name', 'age'])
persons: List[Person] = [
    Person('g', 25),
    Person('j', 30),
    Person('m', 15)
]

older_person = persons[0]
for person in persons:
    if person.age > older_person.age:
        older_person = person

print('Max age is', older_person.age)
older_person = max(persons)
print(older_person)
older_person = max(persons, key=lambda person: person.age)
print(older_person)
# função anónima -> não tem nome

# map


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'Person(name={self.name}, age={self.age})'


persons: List[Person] = [
    Person('g', 25),
    Person('j', 30),
    Person('m', 15)
]


def pass_year(persons: List[Person]):
    # older_persons = []
    # for person in persons:
    #    older_person.append(Person(person.name, person.age+1))
    # return older_persons
    return list(map(lambda person: Person(person.name, person.age+1), persons))


pprint(persons)
pprint(pass_year(persons))

some_list = [1, 2, 3, 4]
print(list(map(lambda n: n*'*', some_list)))

# filter
print(list(filter(lambda n: n % 2 == 0, some_list)))
print(list(filter(lambda person: person.age > 20, persons)))

# listcomp
# more pythonic


def pass_year(persons: List[Person]):
    return [Person(person.name, person.age+1) for person in persons]


print(pass_year(persons))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# equivalent to map
mul_by_2 = [2*n for n in numbers]
# equivalent to filter
divisible_by_2 = [n for n in numbers if n % 2 == 0]
# both
new_numbers = [2*n for n in numbers if n % 2 == 0]
# with if and else
newer_numbers = [2*n if n % 2 != 0 else 3*n for n in numbers]
print(newer_numbers)

# dict comp, set comp
person_dictionary = {person.name: person.age for person in persons}
print(person_dictionary)
person_set = {person.name for person in persons}
print(person_set)

# genexp
genexp_numbers = (2*n for n in numbers)
print(genexp_numbers, type(genexp_numbers))
print(next(genexp_numbers))
print(next(genexp_numbers))
print(next(genexp_numbers))
for n in genexp_numbers:
    print(n)
genexp_numbers = (2*n for n in numbers)
for n in genexp_numbers:
    print(n)
# try next(genexp_numbers)

genexp_numbers = (2*n for n in numbers)
print(getsizeof(genexp_numbers))
print(getsizeof(numbers))
big_list = list(range(10000))
big_genexp = (2*n for n in big_list)
print(f'bigList: {getsizeof(big_list)}bytes')
print(f'bigGenexp: {getsizeof(big_genexp)}bytes')
# Conclusion: great when we only need consumption one by one
# Memory waste, not to mention time. Just think when
# we're dealing with big big data (GBytes, e.g.)

# generators with more lines


def my_generator(size: int, filter_func) -> Generator:
    n = 0
    while n < size:
        if filter_func(n):
            yield n
        n += 1


my_gen = my_generator(100000, lambda n: n % 23 == 0 or n % 123 == 0)
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
for n in my_gen:
    print(n)

#
# if we have time, 5. itertools
# remember this is func programming

# count()
infinite_counter = itertools.count(2, 2)
print(next(infinite_counter), next(infinite_counter))
print(next(infinite_counter), next(infinite_counter))
# try infinite iteration

# cycle()
infinite_cycle = itertools.cycle('123456')
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))
print(next(infinite_cycle), next(infinite_cycle))

###### takewhile
#####my_list = [1, 2, 3, 4, 5]
#####gen = itertools.takewhile(lambda n: n < 4, my_list)
#####print(next(gen))
#####print(next(gen))
#####print(next(gen))
###### print(next(gen)) # explodes
#####gen = itertools.takewhile(lambda n: n*73 % 12300 != 2, itertools.count(1))
#####for i in gen:
#####    print(i)
#####
###### combinations()
#####gen = itertools.combinations(range(4), 3)
#####print(*list(gen), sep='\n')
###### permutations()
#####gen = itertools.permutations(range(4), 3)
#####print(*list(gen), sep='\n')
