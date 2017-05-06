from phpmyadmin import phpmyadmin_main
from termcolor import colored

VERSION = '0.0.0'


def main():
    """Entry point for the application script"""
    print
    print(colored("VERSION: %s" % VERSION, 'blue'))
    print(colored("ITS A DUMMY YET", 'blue'))
    print(colored("Wait for Version >= 0.0.1", 'blue'))
    print
    phpmyadmin_main()
