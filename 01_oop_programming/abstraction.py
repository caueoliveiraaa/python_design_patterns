""" This file contains examples of abstraction (OOP) """
from abc import ABC, abstractmethod


class Payment(ABC):
    """
    Abstract class representing a payment method.

    Methods:
        process_payment(amount): Abstract method to be implemented by subclasses.
    """
    @abstractmethod
    def process_payment(self, amount) -> None:
        """ Abstract method to be implemented by subclasses. """
        return None


class CreditCard(Payment):
    """
    Concrete class representing payment via credit card.

    Methods:
        process_payment(amount): Implements credit card payment processing.
    """
    def process_payment(self, amount):
        print(f"[CreditCard] Processing payment of ${amount:.2f} via credit card.")


class ViaPix(Payment):
    """
    Concrete class representing payment via pix.

    Methods:
        process_payment(amount): Implements pix payment generation.
    """
    def process_payment(self, amount):
        print(f"[Pix] Generating pix for payment of ${amount:.2f}.")


def display_example() -> None:
    """ Displays an exmaple of encapsulation. """
    print("\n--- Starting payments ---")
    payment_methods = [
        CreditCard(),
        ViaPix()
    ]

    for method in payment_methods:
        method.process_payment(150.00)


if __name__ == '__main__':
    display_example()
