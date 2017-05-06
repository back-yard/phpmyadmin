import os
from ConfigParser import ConfigParser, NoOptionError
from termcolor import colored


def get_config():
    return __read_config()


def __get_attr(parser, name, default=''):
    try:
        return parser.get('config', name)
    except NoOptionError:
        return default


def __read_config():
    config_file = "%s/.phpmyadmin" % os.path.expanduser('~')
    if os.path.isfile(config_file):
        config = dict()
        c_parser = ConfigParser()
        c_parser.read(config_file)

        config['host'] = __get_attr(c_parser, 'host', 'localhost')
        config['port'] = __get_attr(c_parser, 'port', '3306')
        config['user'] = __get_attr(c_parser, 'user', 'root')
        config['pass'] = __get_attr(c_parser, 'pass', '')
        config['image_version'] = __get_attr(c_parser, 'image_version', 'latest')

        return config
    else:
        print(colored("Config file not found.", 'red'))
        print(colored("Please create the file '~/.phpmyadmin' in your home directory", 'red'))
        return None
