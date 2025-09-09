"""
This file contains examples of encapsulation (OOP).

Base Class (Animal): Defines shared attributes and behaviors.
Derived Classes (Dog, Cat): Inherit from Animal and override the make_sound() method.
Polymorphism: The same method name (make_sound) behaves differently depending on the object's class.
"""


class Animal:
    """
    Base class representing a generic animal.

    Attributes:
        name (str): The name of the animal.

    Methods:
        make_sound(): Prints a generic message about the animal's sound.
    """
    def __init__(self, name):
        self.name = name
        print(f"[Animal] Creating an animal named {self.name}")

    def make_sound(self):
        """ Makes a sound in the form of printing. """
        print(f"[Animal] {self.name} makes a generic sound.")


class Dog(Animal):
    """
    Class representing a dog, inherits from Animal.

    Methods:
        make_sound(): Prints the specific sound a dog makes.
    """
    def make_sound(self):
        """ Makes a sound for a dog in the form of printing. """
        print(f"[Dog] {self.name} says: Woof woof!")


class Cat(Animal):
    """
    Class representing a cat, inherits from Animal.

    Methods:
        make_sound(): Prints the specific sound a cat makes.
    """
    def make_sound(self):
        """ Makes a sound for a cat in the form of printing. """
        print(f"[Cat] {self.name} says: Meow!")


def display_example() -> None:
    """ Displays an exmaple of heritage. """
    print("\n--- Creating animals ---")
    generic_animal = Animal("Creature")
    dog = Dog("Rex")
    cat = Cat("Mimi")

    print("\n--- Making sounds ---")
    generic_animal.make_sound()
    dog.make_sound()
    cat.make_sound()


if __name__ == '__main__':
    display_example()
