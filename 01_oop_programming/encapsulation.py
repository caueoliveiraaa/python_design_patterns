""" 
This file contains examples of encapsulation (OOP).
Encapsulation is the practice of hiding internal state and requiring all
interactions to be performed through an object's methods. This protects
the integrity of the data and promotes modular design.
"""
from uuid import uuid4


class User:
    """ Represents a user in the system. """
    def __init__(self, name: str, email: str, password: str):
        """
        Constructor of the User class.
        
        Trying to access self.__password or self.__online directly will throw an error
        of the type AttributeError.
        
        Encapsulation in Python is done with __:
        """
        self.online: bool = False
        self.name: str = name
        self.email: str = email
        self.__password: str = password
        self.__id = uuid4()

    def log_into_website(self) -> None:
        """ Logs into the website. """
        if self.__validate_credentials():
            self.online = True
            print('Logged into the website successfully')
        else:
            raise ValueError('User does not have the necessary credentials')

    def log_out_website(self) -> None:
        """ Logs out of the website. """
        if self.__validate_credentials():
            self.online = False
            print('Logged out of the website successfully')
        else:
            raise ValueError('User does not have the necessary credentials')

    def is_online(self) -> bool:
        """ Checks if the user is online. """
        return bool(self.online)
    
    def display_user_id(self) -> bool:
        """ Display the ID of the user. """
        return print(f'User id: {self.__id}')

    def __validate_credentials(self) -> bool:
        """ Checks if credentials are empty. """
        return bool(self.email and self.__password)


def display_example() -> None:
    """ Displays an exmaple of encapsulation. """
    user = User(name='User', email='user@example.com', password='123')
    user.log_into_website()
    print(f'User is online: {user.is_online()}')
    user.log_out_website()
    print(f'User is online: {user.is_online()}')
    user.display_user_id()


if __name__ == '__main__':
    display_example()
