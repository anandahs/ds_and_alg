from ordered_set import OrderedSet
import time
from functools import wraps
import datetime


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age)


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"execution time of {func.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper


def two_sums(student_scores, target):
    seen = {}

    for key, score in enumerate(student_scores):

        compliment = target - score

        if compliment in seen:
            return seen[compliment], key
        seen[score] = key
    return -1, -1


@time_it
def remove_duplicates(items):
    unique_lst = list()
    seen = set()

    for item in items:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst


@time_it
def remove_duplicates_1(items):
    return list(OrderedSet(items))


if __name__ == "__main__":
    scores = [85, 86, 92, 108, 91, 85]
    print(two_sums(scores, 199))

    items1 = list()

    for i in range(1000000):
        items1.append(i)
        items1.append(i)
    #
    # print(remove_duplicates(items1))
    # print(remove_duplicates_1(items1))

    remove_duplicates(items1)
    remove_duplicates_1(items1)

    Ananda_person = Person.from_birth_year('Ananda', 1986)
    print(Ananda_person.age)

    Atharva_person = Person.from_birth_year('Atharva', 2018)
    print(Atharva_person.age)
