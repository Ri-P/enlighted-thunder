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
import docopt
import sys

import ethunder

__author__ = "Richard Pfeifer"


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


def Main():
    parse_commandline(sys.argv[1:])

    try:
        print("Hello world. This is ethunder!")
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
    sys.exit(0)

if __name__ == "__main__":
    Main()
