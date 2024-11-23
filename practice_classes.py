class Youtube:

    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


user1 = Youtube("Ananda")
user2 = Youtube("Chethana")

print(f"user1:{user1.__dict__}")
print(f"user1:{user2.__dict__}")

user1.subscribe(user2)

print(f"user1:{user1.__dict__}")
print(f"user1:{user2.__dict__}")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def from_class(cls, data):
        return cls(data['title'], data['author'], data['pages'])


data = {
    'title': 'man who overcame health issues',
    'author': 'tamboori',
    'pages': 56
}

book1 = Book.from_class(data=data)
print(book1.__dict__)

from datetime import date


class Person:

    @staticmethod
    def get_age(birth_year) -> int:
        today = date.today()
        age = today.year - birth_year
        return age

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = cls.get_age(birth_year)
        return cls(name, age)


person1 = Person.from_birth_year("Ananda", 1986)
person2 = Person.from_birth_year("Atharv", 2018)
person3 = Person.from_birth_year("Aarav", 2019)

print(person1.__dict__)
print(person2.__dict__)
print(person3.__dict__)


class Counter:
    count = 0

    def __init__(self):
        self.increment()

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


# Usage
c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())  # Output: 2
