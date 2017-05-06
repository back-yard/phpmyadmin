import sys

from support import check_docker, get_config, get_docker_version, check_image, pull_image
from termcolor import colored

IMAGE_NAME = 'phpmyadmin/phpmyadmin'


def get_valid_config():
    config = get_config()
    if config is None:
        sys.exit(1)
    if not check_docker():
        sys.exit(1)

    return config


def phpmyadmin_main():
    config = get_valid_config()

    if not check_image(IMAGE_NAME, config.get('image_version')):
        print(pull_image(IMAGE_NAME, config.get('image_version')))

    print(colored("image ok :)", 'green'))
