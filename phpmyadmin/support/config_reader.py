import os
from ConfigParser import ConfigParser
from termcolor import colored


def get_config():
    return __read_config()


def __read_config():
    config_file = "%s/.phpmyadmin" % os.path.expanduser('~')
    if os.path.isfile(config_file):
        config = dict()
        c_parser = ConfigParser()
        c_parser.read(config_file)
        config['host'] = c_parser.get('config', 'host')
        config['port'] = c_parser.get('config', 'port')
        config['user'] = c_parser.get('config', 'user')
        config['pass'] = c_parser.get('config', 'pass')
        return config
    else:
        print(colored("Config file not found.", 'red'))
        print(colored("Please create the file '~/.phpmyadmin' in your home directory", 'red'))
        return None
