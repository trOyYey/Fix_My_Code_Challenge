#!/usr/bin/python3
""" 
User class
"""

class User():
    """ User class """

    def __init__(self):
        """ instance initialization """
        self.__email = None
    @property
    def email(self):
        """ email getter attribute """
        return self.__email

    @email.setter
    def email(self, value):
        """ email setter attribute """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
