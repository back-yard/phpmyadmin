import sys

from support import get_config


def invoke():
    config = get_config()
    if config is None:
        sys.exit(1)
    else:
        print(config)
