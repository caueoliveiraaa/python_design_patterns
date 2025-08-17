"""
This file contains examples of polymorphism (OOP)
Types of Polymorphism:
    1. Subtype Polymorphism (Classic OOP):
    Allows objects of different classes to be treated
    through the same interface. It's a core concept in object-oriented
    programming that promotes flexibility and reusability.

    2 - Parametric Polymorphism (Behavior changes based on input):
    In languages like Java or C++, method overloading (same method name, different parameters)
    is a formal feature. Python doesn’t support it natively, but you can simulate it:
    
Expected output:
    >> Calling method speak with the Brazilian class:
    >> Aqui falamos Brasileiro
    >> Calling method speak with the Mexican class:
    >> Aquí se habla Español de México
    >> Hello, User 1
    >> ['Hello, User 2', 'Hello, User 3', 'Hello, User 4']
"""
from typing import Union


class Comunicator:
    """ Base class / Abstract interface for comunicators. """
    def speak(self):
        """ Base method for speaking. """
        raise NotImplementedError('A subclass has to implement this method')


class Brazilian(Comunicator):
    """ Represents a Brazilian speaker. """
    def speak(self):
        """ Speaks Brazilian Porguese. """
        print('Aqui falamos Brasileiro')


class Mexican(Comunicator):
    """ Represents a Mexican speaker. """
    def speak(self):
        """ Speaks Mexican Spanish. """
        print('Aquí se habla Español de México')


def greet_user(usernames: Union[str, list]) -> str:
    """ Greets a new user or new users, depending on the arguments. """
    if isinstance(usernames, list):
        return [f"Hello, {name}" for name in usernames]
    return f"Hello, {usernames}"


def displays_example_subtypes():
    """ Displays examples of polymorphism with subtypes. """
    brazilian = Brazilian()
    mexican = Mexican()
    print('Calling method speak with the Brazilian class:')
    brazilian.speak()
    print('Calling method speak with the Mexican class:')
    mexican.speak()


if __name__ == '__main__':
    displays_example_subtypes()
    print(greet_user(usernames='User 1'))
    print(greet_user(usernames=['User 2', 'User 3', 'User 4']))
