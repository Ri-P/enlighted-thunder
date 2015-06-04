# -*- coding: utf-8 -*-
"""
Usage:
    ethunder
    ethunder -h | --help
    ethunder --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""
from __future__ import print_function
from __future__ import unicode_literals
import os.path
import sys

import docopt
import ethunder
from ethunder.config import configurate

__author__ = "Richard Pfeifer"


class EThunderError(Exception):
    pass


def parse_commandline(argv):
    """
    Let docopt handle the CLI and return dict of arguments.
    """
    try:
        # Parse arguments
        arguments = docopt.docopt(__doc__, argv,
                                  version=ethunder.__version__)
    except docopt.DocoptExit as e:
        print(e.message)
        sys.exit(0)
    return arguments


def print_message():
    awesome_negation = "not "
    if ethunder.config["is_awesome"]:
        awesome_negation = ""
    msg = (
        "Hello world. This is ethunder and it is {0}awesome!\n"
        "\tRainbow can be found at: {1}\n"
        "\tvalue1 = {2}"
    ).format(
        awesome_negation,
        os.path.normpath(ethunder.config["path_to_rainbow"]),
        ethunder.config["value1"]
    )
    print(msg)


def Main():
    parse_commandline(sys.argv[1:])

    try:
        configurate()
        print_message()
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
    sys.exit(0)

if __name__ == "__main__":
    Main()
