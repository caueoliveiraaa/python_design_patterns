""" 
This file contains examples of encapsulation (OOP).
Encapsulation is the practice of hiding internal state and requiring all
interactions to be performed through an object's methods. This protects
the integrity of the data and promotes modular design.
"""


class User:
    """ Represents a user in the system. """
    def __init__(self, name: str, email: str, password: str):
        """
        Constructor of the class.
        Trying to access self.__password or self.__online directly will throw an error
        of the type AttributeError.
        """
        self.name = name
        self.email = email
        # Encapsulation in Python is done with __:
        self.__password = password
        self.__online = False

    def log_into_website(self) -> None:
        """ Logs into the website. """
        if self.__validate_credentials():
            self.__online = True
            print('Logged into the website successfully.')
            return
        raise ValueError('User does not have the necessary credentials.')

    def log_out_website(self) -> None:
        """ Logs out of the website. """
        if self.__validate_credentials():
            self.__online = False
            print('Logged out of the website successfully.')
            return
        raise ValueError('User does not have the necessary credentials.')

    def is_online(self) -> bool:
        """ Checks if the user is online. """
        return bool(self.__online)

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


if __name__ == '__main__':
    display_example()
