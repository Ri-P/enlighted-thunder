# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nose.tools import assert_equal, assert_raises

import ethunder
import ethunder.app as app
from ethunder.test.testutils import captured_out

__author__ = "Richard Pfeifer"


def test_garbageargument():
    """
    Do SystemExit and show 'usage' for bad CLI-arguments.
    """
    argv = ['--garbage in ']
    expected_output = ("Usage:\n    ethunder\n"
                       "    ethunder -h | --help\n"
                       "    ethunder --version\n")

    with captured_out() as (out, err):
        with assert_raises(SystemExit):
            app.parse_commandline(argv)
        assert_equal(expected_output, out.getvalue())


def test_versionstring():
    """
    CLI-call '>ethunder --version' should print correct version.
    """
    argv = ['--version']
    expected_output = ethunder.__version__
    with captured_out() as (out, err):
        with assert_raises(SystemExit):
            app.parse_commandline(argv)
        assert_equal(expected_output, out.getvalue().strip())
